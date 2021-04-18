from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('items/', views.ItemList.as_view()),
    path('items/<int:pk>', views.ItemDetail.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>', views.CategoryDetail.as_view()),
    path('locations/', views.LocationList.as_view()),
    path('locations/<int:pk>', views.LocationDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
