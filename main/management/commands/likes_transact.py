from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from main.models import *
from common.utils.async import run_chunked_iter
from api.tests import turn_off_auto_now, turn_off_auto_now_add


class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        Find LIKE rows of dish/user occuring > 1 and move to transactional table.
        """
        turn_off_auto_now(LikeTransaction, 'updated')
        turn_off_auto_now_add(LikeTransaction, 'created')
        run_chunked_iter(User.objects.all(), user_loop, num_threads=4)


def user_loop(users):
    for u in users:
        usr_likes = Like.objects.filter(user=u)
        if usr_likes.count() > 100:
            run_chunked_iter(usr_likes, dish_washer, num_threads=1)
        else:
            dish_washer(usr_likes)


def dish_washer(likes):
    for l in likes:
        if Like.objects.filter(user=l.user, dish=l.dish).count() > 1:
            save_the_world(l.user, l.dish)


def save_the_world(user, dish):
    """Move all except latest to LikeTransaction."""
    likes = Like.objects.filter(user=user, dish=dish).order_by('-updated')
    for l in likes[1:]:
        try:
            like_trans, created = LikeTransaction.objects.get_or_create(
                user=l.user, dish=l.dish, did_like=l.did_like,
                created=l.created, updated=l.updated
            )
        except LikeTransaction.MultipleObjectsReturned:
            pass
        l.delete()
