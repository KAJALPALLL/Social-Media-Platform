from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from recipe_management.models import Recipe, Rating
from django.contrib.auth.models import User
from .tasks import compress_image_task

class RecipeSerializer(ModelSerializer):
    name = serializers.CharField()
    image = serializers.ImageField()
    description = serializers.CharField()

    class Meta:
        model = Recipe
        fields = ["id", "name", "image", "description"]

    def create(self, validated_data):
        recipe = Recipe.objects.create(**validated_data)
        compress_image_task.delay(recipe.id)
        return recipe

class RatingSerializer(ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    recipe = serializers.PrimaryKeyRelatedField(queryset=Recipe.objects.all())
    stars = serializers.IntegerField()

    class Meta:
        model = Rating
        fields = ["customer", "recipe", "stars"]
