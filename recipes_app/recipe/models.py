from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=30)
    image_url = models.URLField()
    description = models.TextField()
    ingredients = models.CharField(max_length=500)
    time = models.IntegerField()

    def __str__(self):
        return f'{self.title}'
