from rest_framework import serializers
from .models import Apartment, RentData

class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = ('id', 'address', 'city', 'state', 'apartment_type', 'amenities')

class RentDataSerializer(serializers.ModelSerializer):
    apartment = ApartmentSerializer()  # Nesting the Apartment serializer
    class Meta:
        model = RentData
        fields = ('id', 'income_bracket', 'apartment', 'rent_amount', 'lease_start_date', 'lease_end_date', 'rent_paid_date')
