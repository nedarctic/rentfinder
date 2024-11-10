from rest_framework import generics
from .models import RentData, Apartment
from .serializers import RentDataSerializer, ApartmentSerializer

class ListApartment(generics.ListAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer

class DetailApartment(generics.RetrieveAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer

class ListRentData(generics.ListAPIView):
    queryset = RentData.objects.all()
    serializer_class = RentDataSerializer

class DetailRentData(generics.RetrieveAPIView):
    queryset = RentData.objects.all()
    serializer_class = RentDataSerializer
