from .models import Product
from rest_framework import serializers
# from Hotelapp.serializers import Hotelserializer


class ProductSerializer(serializers.ModelSerializer):
    # hotel = Hotelserializer(read_only=True)   this line is used to display the hotel name instead of hotel id

    class Meta:
        model = Product
        fields = '__all__'
        # fields = ['name', 'price', 'category', 'hotel']


# class HotelProductSerializer(serializers.ModelSerializer):
#     Hotel = Product(source='Hotel_set')
#     class Meta:
#         model = Product
#         fields = '__all__'
