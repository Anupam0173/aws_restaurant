from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

# http://127.0.0.1:8000/product/pview/2/


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
