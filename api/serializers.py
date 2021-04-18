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
    category = CategorySerializer(
        allow_null=True, required=False, read_only=False)
    location = LocationSerializer(
        allow_null=True, required=False, read_only=False)

    class Meta:
        model = Item
        fields = ['id', 'description', 'in_use', 'replacement_link',
                  'replacement_cost', 'created_at', 'updated_at', 'category', 'location']

    def create(self, validated_data):
        (validated_data, category_data,
         location_data) = self.get_relationship_fields(validated_data)
        item = Item.objects.create(**validated_data)

        self.handle_category_field(category_data, item)
        self.handle_location_field(location_data, item)

        return item

    def update(self, instance, validated_data):
        (validated_data, category_data,
         location_data) = self.get_relationship_fields(validated_data)

        self.handle_category_field(category_data, instance)
        self.handle_location_field(location_data, instance)

        instance.description = validated_data.get(
            'description', instance.description)
        instance.in_use = validated_data.get('in_use', instance.in_use)
        instance.replacement_link = validated_data.get(
            'replacement_link', instance.replacement_link)
        instance.replacement_cost = validated_data.get(
            'replacement_link', instance.replacement_cost)
        instance.save()

        return instance

    def get_relationship_fields(self, validated_data):
        category_data = None
        location_data = None
        if validated_data.get('location'):
            location_data = validated_data.pop('location')
        if validated_data.get('category'):
            category_data = validated_data.pop('category')
        return (validated_data, category_data, location_data)

    def handle_category_field(self, category_data, item):
        if category_data is not None:
            category = Category.objects.filter(
                name=category_data['name']).first()
            if category is None and category_data.get('name') is not None:
                category = Category.objects.create(**category_data)
            category.item_set.add(item)
        else:
            category = item.category
            if category is None:
                return
            else:
                category.item_set.remove(item)
                item.category = None
                item.save()
        return

    def handle_location_field(self, location_data, item):
        if location_data is not None:
            location = Location.objects.filter(
                name=location_data['name']).first()
            if location is None and location_data.get('name') is not None:
                location = Location.objects.create(**location_data)
            location.item_set.add(item)
        else:
            location = item.location
            if location is None:
                return
            else:
                location.item_set.remove(item)
                item.location = None
                item.save()
        return
