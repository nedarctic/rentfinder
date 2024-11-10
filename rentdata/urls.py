from django.urls import path
from .views import ListRentData, DetailRentData

urlpatterns = [    
    path('rentdata/<int:pk>/', DetailRentData.as_view(), name='rentdata-detail'),
    path('rentdata/', ListRentData.as_view(), name='rentdata-list'),
]