from django.urls import path
from . import views

urlpatterns =[
    path('<int:pk>', views.ProductsDetailAPIView.as_view()),
    path('', views.ProductsListCreateAPIView.as_view()),
    # path('list/', views.ProductsListAPIView.as_view())
]