from rest_framework import generics

from products.models import Products
from products.models import ProductsManager
from products.serializers import ProductsSerializer

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
        