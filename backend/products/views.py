# from django.shortcuts import render
from rest_framework import generics
from . models import Products
from . serializers import ProductsSerializer


class ProductsDetailAPIView(generics.RetrieveAPIView):
    
    # queryset attibute must be used to query db in generic views
    queryset = Products.objects.all()    
    # serializer_class attibute must be used to serialize data in json for the client          
    serializer_class = ProductsSerializer



