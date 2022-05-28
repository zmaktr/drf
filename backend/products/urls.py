from django.urls import path
from . import views

urlpatterns =[
    # class based views DRF
    path('', views.ProductsListCreateAPIView.as_view()),
    path('<int:pk>', views.ProductsDetailAPIView.as_view()),    
    path('<int:pk>/update/', views.ProductsUpdateAPIView.as_view()),
    path('<int:pk>/delete/', views.ProductsDeleteAPIView.as_view()),

    # function based views DRF
    # path('<int:pk>', views.products_alt_view),
    # path('', views.products_alt_view),
]