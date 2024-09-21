from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from django.http import HttpResponseNotFound

from .models import Recipe, User
from .serializers import RecipieSerializer, UsernameUpdateSerializer


class ListCreateRecipe(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipieSerializer


class RecipeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipieSerializer


class VerifyEmailView(APIView):
    def get(self, request, *args, **kwargs):
        key = kwargs.get("key")
        data = {"key": key}
        return Response(data, status=status.HTTP_200_OK)
    
class PasswordResetView(APIView):
    def get(self, request, *args, **kwargs):
        uid = kwargs.get('uidb64', None)
        key = kwargs.get('key', None)
        data = {'uid': uid, 'token': key}
        return Response(data, status=status.HTTP_200_OK)


class UpdateUsernameView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = UsernameUpdateSerializer

    def get_object(self):
        return self.request.user
    
class ValidateUsername(APIView):  # Might be realtime later
    def get(self, request):
        username = request.query_params.get('username', None)
        if User.objects.filter(username=username).exists():
            data = {'username': 'username is taken.'}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        data = {'detail': 'username is available'}
        return Response(data, status=status.HTTP_200_OK)
    
class ValidateEmail(APIView):
    def get(self, request):
        email = request.query_params.get('email', None)
        if User.objects.filter(email=email).exists():
            data = {'email': 'An account was found with this email'}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        data = {'detail': 'email is valid'}
        return Response(data, status=status.HTTP_200_OK)


class NotFoundView(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponseNotFound()
