from django.urls import path
from recipes_app.recipe.views import index
from recipes_app.recipe.views import detail_recipe
from recipes_app.recipe.views import create_recipe
from recipes_app.recipe.views import edit_recipe
from recipes_app.recipe.views import delete_recipe

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_recipe, name='create recipe'),
    path('edit/<int:pk>', edit_recipe, name='edit recipe'),
    path('delete/<int:pk>', delete_recipe, name='delete recipe'),
    path('details/<int:pk>', detail_recipe, name='details recipe'),
]

