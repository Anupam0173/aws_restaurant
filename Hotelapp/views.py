
from django.shortcuts import render
from rest_framework import viewsets
from .models import Hotel
from Productapp.models import Product
from Productapp.serializers import ProductSerializer
from .serializers import HotelSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# http://127.0.0.1:8000/hotel/hview/
class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


# http://127.0.0.1:8000/hotel/2/


@api_view(['GET'])
def particular_hotel_products(request, id):
    try:
        hotel_products = Product.objects.filter(hotel_id=id)
    except Hotel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(hotel_products, many=True)
        return Response(serializer.data)


# class HotelProductSerializer(viewsets.ModelViewSet):
#     queryset = Product.objects.filter()
#     serializer_class = HotelSerializer


# class AllproductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.filter()
#     serializer_class = HotelSerializer
