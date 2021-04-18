from django.urls import path
from api import views

urlpatterns = [
    path('items/', views.item_list),
    path('items/<int:pk>', views.item_detail)
]