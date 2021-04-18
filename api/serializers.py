import logging
from rest_framework import serializers
from .models import Item, Location, Category

logger = logging.getLogger(__name__)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at', 'updated_at']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'created_at', 'updated_at']


class ItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(allow_null=True, read_only=False)
    location = LocationSerializer(allow_null=True, read_only=False)

    class Meta:
        model = Item
        fields = ['id', 'description', 'in_use', 'replacement_link',
                  'replacement_cost', 'created_at', 'updated_at', 'category', 'location']

    def create(self, validated_data):
        location_data = validated_data.pop('location')
        category_data = validated_data.pop('category')
        item = Item.objects.create(**validated_data)

        # Note/TODO: running into an issue where I cannot provide a null category/location field to unset/prevent setting the relation, despite having null and blank fields defined
        category = Category.objects.filter(name=category_data['name']).first()
        if category is None and category_data.get('name') is not None:
            category = Category.objects.create(**category_data)
        category.item_set.add(item)

        return item

    def update(self, instance, validated_data):
        location_data = validated_data.pop('location')
        category_data = validated_data.pop('category')

        # If the location field is provided, we want to:
        # 1. Check if the instance has an existing location relationship
        # 2. If it does, check if the location name and relationship match
        # 3. If they don't match, find the provided location and attach it

        location = Location.objects.filter(
            name=location_data['location']).first()

        # If the location field is not provided, remove the relationship entirely

        instance.description = validated_data.get(
            'description', instance.description)
        instance.in_use = validated_data.get('in_use', instance.in_use)
        instance.replacement_link = validated_data.get(
            'replacement_link', instance.replacement_link)
        instance.replacement_cost = validated_data.get(
            'replacement_link', instance.replacement_cost)

        return instance
