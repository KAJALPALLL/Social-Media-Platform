from .views import RecipeAPIView, RatingAPIView
from django.urls import path

urlpatterns = [
    path('rating', RatingAPIView.as_view()),
    path('recipe', RecipeAPIView.as_view()),
]