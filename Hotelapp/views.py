
from django.shortcuts import render
from rest_framework import viewsets
from .models import Hotel
from Productapp.models import Product
from Productapp.serializers import ProductSerializer
from .serializers import HotelSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# http://127.0.0.1:8000/hotel/hview/            for hotel crud operation
class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


# http://127.0.0.1:8000/hotel/2/        for listing all products of partiular hotel.
@api_view(['GET'])
def particular_hotel_products(request, id):
    try:
        hotel_products = Product.objects.filter(hotel_id=id)
    except Hotel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(hotel_products, many=True)
        return Response(serializer.data)


# class HotelProduct(viewsets.ModelViewSet):
#     queryset = Product.objects.filter(hotel_id=id)
#     serializer_class = ProductSerializer


# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def product_detail(request, pk):
#     try:
#         hotel_products = Product.objects.filter(hotel_id=id)
#     except Hotel.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ProductSerializer(hotel_products, many=True)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = ProductSerializer(hotel_products, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,
#                         status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'PATCH':
#         serializer = ProductSerializer(
#             hotel_products, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,
#                         status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         hotel_products.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class AllproductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.filter()
#     serializer_class = HotelSerializer
