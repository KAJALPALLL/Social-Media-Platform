from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='recipes/')
    description = models.TextField()

class Rating(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    stars = models.PositiveSmallIntegerField()
