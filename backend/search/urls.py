from django.urls import path, include

from . import views 

urlpatterns= [
    path('', views.SearchListView.as_view(), name='search') ,
    path('algolia/', views.SearchListViewAPI.as_view(), name='search_algolia') 
]