from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin


class User(AbstractUser, PermissionsMixin):
    address = models.CharField(max_length=300, null=True)
    bio = models.TextField(null=True)

    def __str__(self) -> str:
        return f"<User {self.first_name}>"

    class Meta:
        db_table = "user"


class Recipe(models.Model):
    name = models.CharField(max_length=150, null=False)
    description = models.TextField(max_length=260, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "recipe"
