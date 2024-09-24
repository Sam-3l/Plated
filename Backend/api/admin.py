from django.contrib import admin
from .models import User

class Admin(admin.ModelAdmin):
    list_display = ["username", "pk", "first_name", "email"]

admin.site.register(User, Admin)