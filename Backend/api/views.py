from database.models import Recipe, RecipeRatingsAndReviews, User
from .serializers import RecipeSerializer, PublicUserSerializer,PublicRecipeSerializer, RatingsAndReviewsSerializer

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.decorators import action
from django.db import IntegrityError

class RecipeViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    serializer_class = RecipeSerializer

    def get_queryset(self):
        if self.action in ['public_list', 'public_details', 'save', 'saves',]:  # All recipes for public actions
            return Recipe.objects.select_related('author').all()
        return Recipe.objects.filter(author=self.request.user).select_related('author').all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=False, methods=['get',], permission_classes=[AllowAny,], url_path='public-list')
    def public_list(self, request):
        """
        Public Recipe View - with read-only access to all recipes. 
        Accessible to all users (even unauthenticated users)
        """
        recipes = self.get_queryset()
        serializer = PublicRecipeSerializer(recipes, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get',], permission_classes=[AllowAny,], url_path='public-details')
    def public_details(self, request, pk):
        """
        Public Recipe View - with read-only access to specific recipe.
        Accessible to all users (even unauthenticated users)
        """
        recipe = self.get_object()
        serializer = PublicRecipeSerializer(recipe)
        return Response(serializer.data)
    
    @action(detail=True, methods=['patch',], permission_classes=[IsAuthenticated,])
    def save(self, request, *args, **kwargs):
        """
        View to save or un-save recipes.
        Accessible to only authenticated users.
        Saves are private.
        """
        recipe = self.get_object()
        user = request.user
        if user in recipe.saved_by.all():
            recipe.saved_by.remove(user)
            return Response({'detail': 'Recipe unsaved'}, status=status.HTTP_200_OK)
        else:
            recipe.saved_by.add(user)
            return Response({'detail': 'Recipe saved'}, status=status.HTTP_201_CREATED)
        
    @action(detail=False, methods=['get',], permission_classes=[IsAuthenticated,])
    def saves(self, request):
        """
        View to get all recipes saved by a user.
        Clearly, accessible to only authenticated users
        """
        recipes = self.get_queryset().filter(saved_by=request.user)
        serializer = PublicRecipeSerializer(recipes, many=True)
        return Response(serializer.data)

class RatingsAndReviewsViewset(viewsets.ModelViewSet):
    """
    ViewSet to handle ratings and reviews for recipes.
    Reviews are public and visibe to all users.
    """
    serializer_class = RatingsAndReviewsSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        """
        Only show the logged-in user's reviews or all reviews filtered by recipe ID.
        """
        recipe_id = self.request.query_params.get('recipe_id')
        queryset = RecipeRatingsAndReviews.objects.filter(user=self.request.user)  # Only show the user's reviews

        if recipe_id:
            queryset = queryset.filter(recipe__id=recipe_id)

        return queryset

    def perform_create(self, serializer):
        """
        Create or Update a Review (Prevent Duplicates Automatically).
        """
        recipe_id = self.request.data.get('recipe_id')
        if not recipe_id:
            raise serializers.ValidationError({"error": "Recipe ID is required"})

        try:
            recipe = Recipe.objects.get(id=recipe_id)
        except Recipe.DoesNotExist:
            raise serializers.ValidationError({"error": "Recipe not found"})

        # Check if the user already reviewed this recipe
        existing_review = RecipeRatingsAndReviews.objects.filter(
            user=self.request.user, recipe=recipe
        ).first()

        if existing_review:
            # If review already exists, update the existing review instead of creating a new one
            serializer.instance = existing_review
            return self.perform_update(serializer)

        try:
            serializer.save(user=self.request.user, recipe=recipe)
        except IntegrityError:
            raise serializers.ValidationError({"error": "You've already reviewed this recipe"})

    def perform_update(self, serializer):
        """
        Update Only the Logged-In User's Review.
        """
        instance = serializer.instance

        if instance.user != self.request.user:
            raise serializers.ValidationError(
                {"error": "You can only edit your own reviews"}
            )

        recipe = instance.recipe

        serializer.save(user=self.request.user, recipe=recipe)

    def destroy(self, request, *args, **kwargs):
        """
        Only Allow Users to Delete Their Own Reviews.
        """
        instance = self.get_object()
        if instance.user != request.user:
            return Response(
                {"error": "You can only delete your own reviews"},
                status=status.HTTP_403_FORBIDDEN
            )
        self.perform_destroy(instance)
        return Response({"message": "Review deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class PublicUserViewSet(viewsets.ModelViewSet):
    """
    Public user viewset for public profile view and follow.
    Assessible to all users but only authenticated users can follow/unfollow.
    """
    queryset = User.objects.all()
    serializer_class = PublicUserSerializer

    http_method_names = ['get',]

    @action(methods=['patch',], detail=True, permission_classes=[IsAuthenticated,])
    def follow(self, request):
        """
        View to follow and unfollow a user.
        """
        user = self.get_object()
        auth_user = request.user
        if auth_user in user.followers.all():
            user.followers.remove(auth_user)
            return Response({'detail': f'{user.username} unfollowed'}, status=status.HTTP_200_OK)
        else:
            user.followers.add(auth_user)
            return Response({'detail': f'{user.username} followed'}, status=status.HTTP_201_CREATED)

    @action(methods=['get',], detail=True, permission_classes=[AllowAny,])
    def followers(self, request):
        """
        View to get list of a user's followers.
        Anyone can access this.
        """
        user = self.get_object()
        followers = User.objects.filter(following=user)
        serializer = PublicUserSerializer(followers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['get',], detail=True, permission_classes=[AllowAny,])
    def following(self, request):
        """
        View to get list of a user's following => All the users the queried user is following.
        Anyone can access this.
        """
        user = self.get_object()
        following = User.objects.filter(followers=user)
        serializer = PublicUserSerializer(following, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    