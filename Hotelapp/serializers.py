from .models import Hotel
from rest_framework import serializers
from Productapp.serializers import ProductSerializer


class HotelSerializer(serializers.ModelSerializer):
    hotel_product = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        # fields = '__all__'
        fields = ['name', 'address', 'opening_hour',
                  'hotel_product', 'hotel_image']
