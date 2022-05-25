from django.urls import path
from . import views

urlpatterns =[
    path('<int:pk>', views.ProductsDetailAPIView.as_view()),
    path('', views.ProductsCreateAPIView.as_view())
]