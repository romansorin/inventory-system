from .models import Item, Category, Location
from .serializers import ItemSerializer, CategorySerializer, LocationSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics


class ItemList(generics.ListCreateAPIView):
    """
    List all items or create a new item.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, update, or delete an item.
    """
    parser_classes = [MultiPartParser, FormParser]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class CategoryList(generics.ListCreateAPIView):
    """
    List all categories or create a new category.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, update, or delete a category.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class LocationList(generics.ListCreateAPIView):
    """
    List all locations or create a new location.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, update, or delete a location.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
