from django.urls import path
from .views import ListRentData, DetailRentData

urlpatterns = [    
    path('rent-data/<int:pk>/', DetailRentData.as_view(), name='rentdata-detail'),
    path('rent-data/', ListRentData.as_view(), name='rentdata-list'),
]