from django.shortcuts import render
from django.contrib.auth.models import Group, User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user_management.serializer import RegisterSerializer, CustomerSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

Group.objects.get_or_create(name='Customer')
Group.objects.get_or_create(name='Seller')

class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "1", "message": "User registered successfully"})
        return Response({"success": "0", "errors": serializer.errors})

class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                "success": "1",
                "message": "Login successful",
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            })
        else:
            return Response({"success": "0"})

class CustomersAPIView(APIView):
    def get(self, request):
        customers = User.objects.filter(groups__name="Customer")
        serializer = CustomerSerializer(customers, many=True)
        return Response({"success": "1", "data": serializer.data})
