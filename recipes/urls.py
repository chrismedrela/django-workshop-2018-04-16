from django.urls import include, path

import recipes.views

urlpatterns = [
    path('recipe/<str:slug>/', recipes.views.RecipeDetailView.as_view(), name='recipes_recipe_detail'),
    path('create/', recipes.views.RecipeCreateView.as_view(), name='recipes_recipe_create'),
    path('edit/<int:recipe_id>/', recipes.views.RecipeUpdateView.as_view(), name='recipes_recipe_edit'),
    path('', recipes.views.RecipeListView.as_view(), name='recipes_recipe_index'),
]