from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = 'username', 'password'

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(user.password)
        user.save()
        return user


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'
        # fields = 'name', 'price', 'description', 'image', 'category'


class SelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = 'id', 'name'


class SelectionDetailSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field='id', read_only=True)
    items = AdSerializer(many=True)

    class Meta:
        model = Selection
        fields = '__all__'
