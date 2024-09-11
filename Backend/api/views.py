from rest_framework import generics
from .models import Recipe
from .serializers import RecipieSerializer


class ListCreateRecipe(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipieSerializer


class RecipeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipieSerializer
