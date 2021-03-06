from django.test import TestCase, TransactionTestCase
from django.contrib.auth.models import User
from .deduplicator import Deduplicator
from main.models import Ingredient, RecipeIngredient, Recipe, RecipeLike
from django.db.models.functions import Lower
from time import sleep

class TestDeduplicator(TransactionTestCase):
    fixtures = ['fixtures/recipes_with_duplicates2.json']
    needs_cooldown = True

    def tearDown(self):
        sleep(2)

    def setup_user_recipe_likes(self):
        u = User.objects.create(username='bob', email='bob@bob.co')
        u2 = User.objects.create(username='rob', email='rob@bob.co')
        rcps = Recipe.objects.filter(name__in=['foip', 'Test Recipe', 'Blarp'])
        for rcp in rcps:
            u.recipe_likes.add(RecipeLike.objects.create(user=u, did_like=True, recipe=rcp))
        u2.recipe_likes.add(RecipeLike.objects.create(user=u2, did_like=True, recipe=rcps[0]))

    def test_deduplicator_ingredients(self):
        recipe_ingr_count = RecipeIngredient.objects.all().count()
        ingr_count = Ingredient.objects.all().count()
        dd = Deduplicator(Ingredient.objects.all(),
                          'description', Ingredient, Lower)
        dd()
        # Assert it removed ingredients
        ingr_count2 = Ingredient.objects.all().count()
        self.assertLess(ingr_count2, ingr_count)
        # Assert it didn't remove related objects
        self.assertEqual(recipe_ingr_count, RecipeIngredient.objects.all().count())

        dd2 = Deduplicator(Ingredient.objects.all(),
                          'description', Ingredient, Lower)
        dd2()
        self.assertEqual(ingr_count2, Ingredient.objects.all().count())
        self.assertEqual(recipe_ingr_count, RecipeIngredient.objects.all().count())
        # Rerunning deduper should have no effect

    def test_deduplicator_recipes(self):
        self.setup_user_recipe_likes()
        queryset = Recipe.objects.all()
        rcp_cnt = queryset.count()
        class RecipeDeduplicator(Deduplicator):
            queryset = Recipe.objects.all()
            fieldname = 'name'
            model = Recipe
            exclude_relations = ['ingredients', 'keywords', 'tags']

        rdd = RecipeDeduplicator()
        rdd()
        self.assertLess(queryset.count(), rcp_cnt)

