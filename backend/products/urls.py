from django.urls import path
from . import views

urlpatterns =[

    # class based views 
    path('', views.ProductsListCreateAPIView.as_view(), name="product_list"),
    path('<int:pk>/', views.ProductsDetailAPIView.as_view(), name="product_detail"),    
    path('<int:pk>/update/', views.ProductsUpdateAPIView.as_view(), name="product_edit"),
    path('<int:pk>/delete/', views.ProductsDeleteAPIView.as_view()),
    
    # mixins views 
    path('mixinlist/', views.ProductsMixinView.as_view()),
    path('mixindetail/<int:pk>/', views.ProductsMixinView.as_view()),
    path('mixincreate/', views.ProductsMixinView.as_view()),
    path('mixindelete/<int:pk>/', views.ProductsMixinView.as_view()),
    path('mixinupdate/<int:pk>/', views.ProductsMixinView.as_view()),

    # function based views 
    path('<int:pk>/', views.products_alt_view),
    path('', views.products_alt_view),
]