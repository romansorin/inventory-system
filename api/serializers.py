from rest_framework import serializers
from .models import Item, Location, Category


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'description', 'in_use', 'replacement_link',
                  'replacement_cost', 'created_at', 'updated_at']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['name']
