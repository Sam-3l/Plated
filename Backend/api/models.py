from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=150, null=False)
    description = models.TextField(max_length=260, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "recipe"

