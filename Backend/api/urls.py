from django.urls import path
from . import views


urlpatterns = [
    path("recipes/", views.ListCreateRecipe().as_view(), name="list-create-recipe"),
    path("recipes/<int:pk>/", views.RecipeDetailView().as_view(), name="recipe-detail"),
    path("auth/registration/account-confirm-email/<str:key>/", views.VerifyEmailView.as_view(), name="email-verification"), 
    path("auth/registration/account-email-verification-sent/", views.NotFoundView().as_view(), name="not-found"),
    path("auth/username/update/", views.UpdateUsernameView().as_view(), name="update-username"),
    path("auth/reset/<int:uidb64>/<str:key>/", views.PasswordResetView().as_view(), name="password_reset_confirm"),

    path("auth/registration/validate-username/", views.ValidateUsername().as_view(), name="validate-username"),
    path("auth/registration/validate-email/", views.ValidateEmail().as_view(), name="validate-email"),
]
