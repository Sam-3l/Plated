from django.urls import path
from . import  views

urlpatterns = [
    path("", views.ListCreateRecipe().as_view(), name="list-create-recipe")
]
