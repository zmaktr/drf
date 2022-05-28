# from django.shortcuts import render
from rest_framework import generics
from . models import Products
from . serializers import ProductsSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

#-------------------CLASS BASED VIEWS----------------------
class ProductsDetailAPIView(generics.RetrieveAPIView):
    
    # queryset attibute must be used to query db in generic views
    queryset = Products.objects.all()    
    # serializer_class attibute must be used to serialize data in json for the client          
    serializer_class = ProductsSerializer

class ProductsUpdateAPIView(generics.UpdateAPIView):
    
    queryset = Products.objects.all()           
    serializer_class = ProductsSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            
class ProductsDeleteAPIView(generics.DestroyAPIView):
    
    queryset = Products.objects.all()           
    serializer_class = ProductsSerializer

# class ProductsCreateAPIView(generics.CreateAPIView):
class ProductsListCreateAPIView(generics.ListCreateAPIView):
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

# class ProductsListAPIView(generics.ListAPIView):
    
#     queryset = Products.objects.all()              
#     serializer_class = ProductsSerializer


#-------------------FUNCTION  BASED VIEWS----------------------
@api_view(['GET', 'POST'])
# def products_alt_view(request, *args, **kwargs):
def products_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    if method == 'GET':
        pass
        # url_args
        # get request --> detail view
        if pk is not None:
            obj = get_object_or_404(Products, pk=pk)
            data = ProductsSerializer(obj, many=False).data
            return Response(data)
            """
            # queryset = Products.objects.filter(pk=pk)
            # if not queryset.exist():
            #     raise Http404
            # detail view
            """
            return Response()
        else:
        # get request --> list view
            queryset = Products.objects.all()
            data = ProductsSerializer(queryset, many=True).data
            return Response(data)
    if method == 'POST':
        # post request --> create view
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            print(serializer.data)
            return Response(serializer.data)
        return Response({"invalid": "not good dat"}, status=400)   