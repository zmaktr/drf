from rest_framework import viewsets, mixins

from . models import Products
from . serializers import ProductsSerializer

class ProductViewSet(viewsets.ModelViewSet):
    '''
    get -> list --> queryset
    get -> retrieve --> product instance detail view
    post -> create --> new instance
    put -> update
    patch -> partial update
    delete -> destroy
    '''
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    lookup_field = 'pk'

# if you want to use specific html method use mixins
# class ProductGenericViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
#     '''
#     get -> list --> queryset
#     get -> retrieve --> product instance detail view
#     '''
#     queryset = Products.objects.all()
#     serializer_class = ProductsSerializer
#     lookup_field = 'pk'