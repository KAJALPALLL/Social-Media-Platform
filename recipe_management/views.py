from django.shortcuts import render
from recipe_management.models import Recipe
from recipe_management.serializer import RecipeSerializer, RatingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class RecipeAPIView(APIView):
    permissions = [IsAuthenticated]
    def get(self, request):
        recipe = Recipe.objects.all()
        serializer = RecipeSerializer(recipe, many=True)
        return Response({"success": "1", "message": "Recipe fetched successfully", "data": serializer.data})

    def post(self, request):
        if not request.user.groups.filter(name='Seller').exists():
            return Response({"detail": "Only sellers can add recipes."}, status=status.HTTP_403_FORBIDDEN)
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(seller=request.user)
            return Response({"success": "1", "message": "Recipe added successfully"},
                            status=status.HTTP_200_OK)
        else:
            return Response({"success": "0", "message": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)


class RatingAPIView(APIView):
    permissions = [IsAuthenticated]

    def post(self, request):
        if not request.user.groups.filter(name='Customer').exists():
            return Response({"detail": "Only customer can rate recipes."}, status=status.HTTP_403_FORBIDDEN)
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "1", "message": "Ratings added successfully"})
        else:
            return Response({"success": "0", "message": serializer.errors})
