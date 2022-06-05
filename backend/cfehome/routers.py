from rest_framework import routers

from products.viewsets import ProductViewSet #, ProductGenericViewSet

router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='products')

# print(router.urls)
urlpatterns = router.urls


# router = routers.DefaultRouter()
# router.register('products', ProductGenericViewSet, basename='products')

# print(router.get_urls)
# urlpatterns = router.urls