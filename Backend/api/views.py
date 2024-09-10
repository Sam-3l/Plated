from rest_framework.generics import ListCreateAPIView
from .models import Recipe
from .serializers import RecipieSerializer

class ListCreateRecipe(ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipieSerializer
