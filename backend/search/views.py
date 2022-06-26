from rest_framework import generics
from products.models import Products
from products.models import ProductsManager
from products.serializers import ProductsSerializer
from rest_framework.response import Response
from . import client

# search view with algolia api
class SearchListViewAPI(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        user = None
        if request.user.is_authenticated:
            user = request.user.username 
        query = request.GET.get('q')
        print(request.GET.get('public'))
        public = str(request.GET.get('public')) != "0"
        tag = request.GET.get('tag') or None
        if not query:
            return Response('empty query', status=400)
        print(user, query, public, tag)
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
        