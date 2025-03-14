from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

class User(AbstractUser, PermissionsMixin):
    address = models.CharField(max_length=300, null=True)
    bio = models.TextField(null=True)
    is_first_login = models.BooleanField(null=True, default=None)
    profile_image = models.ImageField(upload_to='uploads/profile_images/', blank=True, null=True, default="defaults/profile-default-image.jpeg")
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)
    followers_count = models.PositiveIntegerField(default=0)
    following_count = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f"User: {self.username}"

    class Meta:
        db_table = "user"

class Recipe(models.Model):
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]

    CATEGORY_CHOICES = [
        ('Gluten-Free', 'Gluten-Free'),
        ('Weight Loss', 'Weight Loss'),
        ('Heart Healthy', 'Heart Healthy'),
        # I'll add more categories later
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/recipe_images/', blank=True, null=True, default="defaults/recipe-default-image.png")
    ingredients = models.TextField() 
    # Explanation: -- Formatted text
    # - Each line is formatted as: Ingredient: Quantity | Description or additional info
    # - Optional items are clearly marked
    instructions = models.TextField()
    prep_time = models.PositiveIntegerField(help_text="Time in minutes")
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default="Medium")
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    viewers = models.ManyToManyField(User, related_name='viewed_recipes', blank=True)
    views = models.PositiveIntegerField(default=0)
    saved_by = models.ManyToManyField(User, related_name='saved_recipes', blank=True)
    saves = models.PositiveIntegerField(default=0)
    reviewed_by = models.ManyToManyField(User, through='RecipeRatingsAndReviews', related_name='recipe_reviews')
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0, help_text="Rating from 0.0 to 5.0")
    # NOTE: rating and likes are read only fields, they can't be modified by anyone
    # Their values only get updated from the ratings, likes, comments many to many relationship with this Table (signals). The relationship field can be modified 
    tags = models.CharField(max_length=255, blank=True, help_text="Comma-separated tags for the recipe (e.g. gluten-free, vegan)")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "recipe"

class RecipeRatingsAndReviews(models.Model):
    """
    Intermediate / Through model connecting Recipe and User model for ratings and reviews
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0, help_text="Rating from 0.0 to 5.0")
    comment = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'recipe')
        db_table = "recipe_ratings_and_reviews"

    def __str__(self):
        return f'{self.user.username}\'s review on -> {self.recipe.name}'
    
class RecipeViews(models.Model):
    """
    Intermediate / Through model connecting Recipe and User model for ratings and reviews
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    date_viewed = models.DateTimeField(auto_now_add=True)
