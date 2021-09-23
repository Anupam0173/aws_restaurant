from .models import Product
from rest_framework import serializers

# Create your models here.


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ['name', 'price', 'category']


# class HotelProductSerializer(serializers.ModelSerializer):
#     Hotel = Product(source='Hotel_set')
#     class Meta:
#         model = Product
#         fields = '__all__'
