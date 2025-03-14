from django.db.models.signals import m2m_changed, post_save, post_delete
from django.dispatch import receiver
from django.db.models import Avg
from database.models import Recipe, RecipeRatingsAndReviews, User

@receiver(m2m_changed, sender=Recipe.saved_by.through)
def update_saves(sender, instance, action, **kwargs):
    """
    Automatically update the number of saves (saves field) whenever the saved_by field changes.
    """
    if action in ['post_add', 'post_remove', 'post_clear']:
        instance.saves = instance.saved_by.count()
        instance.save()

@receiver([post_save, post_delete], sender=RecipeRatingsAndReviews)
def update_rating(sender, instance, **kwargs):
    """
    Automatically update the rating (overall rating) of a recipe whenever a rating is added, updated, or deleted.
    """
    recipe = instance.recipe
    ratings = RecipeRatingsAndReviews.objects.filter(recipe=recipe).exclude(rating=0.0)
    average_rating = ratings.aggregate(avg_rating=Avg('rating'))['avg_rating'] or 0
    recipe.rating = average_rating
    recipe.save()

@receiver(m2m_changed, sender=User.followers.through)
def update_followers(sender, instance, action, **kwargs):
    """
    Automatically update the number of followers (followers_count field) whenever the followers m2m field changes.
    """
    if action in ['post_add', 'post_remove', 'post_clear']:
        instance.followers_count = instance.followers.count()
        instance.save()

@receiver(m2m_changed, sender=User.following.through)
def update_following(sender, instance, action, **kwargs):
    """
    Automatically update the number of following (following_count field) whenever the followers m2m field changes.
    """
    if action in ['post_add', 'post_remove', 'post_clear']:
        instance.following_count = instance.following.count()
        instance.save()

def update_views():
    pass