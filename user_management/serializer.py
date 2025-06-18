from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

class RegisterSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=['Customer', 'Seller'])

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        role = validated_data.pop('role')
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        group = Group.objects.get(name=role)
        user.groups.add(group)
        return user

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]