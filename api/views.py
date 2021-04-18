from .models import Item
from .serializers import ItemSerializer
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
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
