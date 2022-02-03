from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    #path('', views.product_list, name='product_list'),
    path('shop/', views.product_list, name='product_list'),
    path('<str:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<str:id>/<str:slug>/', views.product_detail, name='product_detail'),
    
]