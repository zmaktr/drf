from rest_framework import generics
from products.models import Products
from products.models import ProductsManager
from products.serializers import ProductsSerializer
from rest_framework.response import Response
from . import client

# search view with algolia api
class SearchListViewAPI(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        # get variables from search
        tag = request.GET.get('tag') or None
        query = request.GET.get('q')
        if not query:
            return Response('empty query', status=400)
        
        # define facet filter used to narrow down search as deffined in products.index -> settings (public and user)
        public = str(request.GET.get('public')) != "0"
        user = None
        if request.user.is_authenticated:
            user = request.user.username 

        # peform search
        results = client.perform_search(query, tags=tag, user=user, public=public)
        return Response(results)


# search view without algolia api
class SearchListView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    def get_queryset(self, *args, **kwargs):

        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        # print(q)
        results = Products.objects.none()
        
        if q is not None:
            user = None
            if self.request.user.is_authenticated:
                user = self.request.user
            results = qs.search(q, user=user)

        # print(results)
        return results
        