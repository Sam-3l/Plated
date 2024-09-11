from django.urls import path
from . import views

urlpatterns = [
    path("recipes", views.ListCreateRecipe().as_view(), name="list-create-recipe"),  # noqa: E501
    path("recipes/<int:pk>", views.RecipeDetailView().as_view(), name="recipe-detail"),  # noqa: E501
]
