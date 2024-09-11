from rest_framework.serializers import ModelSerializer
from .models import Recipe


class RecipieSerializer(ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'
