# from django.shortcuts import render
from rest_framework import generics
from . models import Products
from . serializers import ProductsSerializer


class ProductsDetailAPIView(generics.RetrieveAPIView):
    
    # queryset attibute must be used to query db in generic views
    queryset = Products.objects.all()    
    # serializer_class attibute must be used to serialize data in json for the client          
    serializer_class = ProductsSerializer

class ProductsCreateAPIView(generics.CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer)
        print(serializer.validated_data)
        print(serializer.validated_data.get('title'))
        # serializer.save()

        # if content is None that assigning title as content
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)


