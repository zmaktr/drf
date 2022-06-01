# django framework
from django.shortcuts import get_object_or_404
# project files
from . models import Products
from . serializers import ProductsSerializer
from . permissions import IsStaffEditorPermission
from api.authentication import TokenAuth
# rest framework
from rest_framework import generics, mixins, permissions, authentication
from rest_framework.decorators import api_view
from rest_framework.response import Response

#-------------------CLASS BASED VIEWS----------------------

# ---retrive---
class ProductsDetailAPIView(generics.RetrieveAPIView): 
    # queryset attibute must be used to query db in generic views
    queryset = Products.objects.all()    
    # serializer_class attibute must be used to serialize data in json for the client          
    serializer_class = ProductsSerializer

# ---update---
class ProductsUpdateAPIView(generics.UpdateAPIView):
    
    queryset = Products.objects.all()           
    serializer_class = ProductsSerializer
    permission_classes = [permissions.DjangoModelPermissions]
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

# ---delete ---
class ProductsDeleteAPIView(generics.DestroyAPIView):

    queryset = Products.objects.all()           
    serializer_class = ProductsSerializer
    lookup_field = 'pk'

    def perform_destory(self, instance):
        super().perform_destroy(instance)

# ---list---
# class ProductsListAPIView(generics.ListAPIView):
#     queryset = Products.objects.all()              
#     serializer_class = ProductsSerializer

# ---create & list combined---
class ProductsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    # authentication_classes = [authentication.SessionAuthentication] # authenticates an exiting user
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication] # authenticates an existing user with token
    # authentication_classes = [authentication.SessionAuthentication, TokenAuth]
    permission_classes = [permissions.IsAdminUser,  IsStaffEditorPermission]
    # permission_classes = [permissions.DjangoModelPermissions]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # permission_classes = [IsStaffEditorPermission]

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



#-------------------MIXINS VIEWS----------------------
# Mixin provide basic view behaviour
class ProductsMixinView(
    mixins.ListModelMixin, 
    mixins.RetrieveModelMixin, 
    mixins.CreateModelMixin, 
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin, 
    generics.GenericAPIView):
    
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    lookup_field = 'pk'
# ---retrive and list---
    def get(self, request, *args, **kwargs):
        print(request)
        print(args, kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        else: 
            return self.list(request, *args, **kwargs)
# ---create---
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
# ---delete---
    def delete(self, request, *args, **kwargs):
        # pk = kwargs.get("pk")
        # if pk is not None:
        return self.destroy(request, *args, **kwargs)
        # else: 
        #     return Response("sdssd")
# ---update---
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


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