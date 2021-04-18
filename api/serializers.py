from rest_framework import serializers
from .models import Item, Location, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at', 'updated_at']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'created_at', 'updated_at']


class ItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    location = LocationSerializer(read_only=True)

    class Meta:
        model = Item
        fields = ['id', 'description', 'in_use', 'replacement_link',
                  'replacement_cost', 'created_at', 'updated_at', 'category', 'location']
