from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^restaurants/((?P<restaurant_slug>[\w\-]+))/', views.restaurant_detail,
        name='restaurant-detail'),
    url(r'^dishes/(?P<dish_id>[0-9]+)/$', views.dish_detail),
    url(r'^dish/(?P<dish_id>[0-9]+)/$', views.dish_detail, name='dish-detail'),
    url(r'^recipe/(?P<recipe_id>[0-9]+)', views.recipe_react, name='recipe-detail'),
    url(r'^recipe/browse/(?P<slug>[\w\-]+)', views.recipe_collection_react, name='recipe-detail'),
    url(r'^blog/', include('blog.urls')),
    url(r'^', include('webapp.flatpages.urls')),
    url(r'^', views.react_app, name='react-app'),
]
