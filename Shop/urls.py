from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('reklama.html', views.reklama, name='reklama'),
    path('cart/', views.cart, name='cart'),
    path('location/', views.location, name='location'),
    # path('categories/', views.category, name='categories'),
    # path('products/<int:pk>', views.products, name='products')
    path('create/product', views.create, name='create'),
    path('cart/', views.cart, name='cart'),
    path('cart/create_order', views.create_order, name='create_order'),
    path('delete_cart_item/<int:pk>', views.delete_cart_item, name='delete_cart_item'),
    path('edit_cart_item/<int:pk>', views.edit_cart_item, name='edit_cart_item'),
    path('orders/', views.orders, name='orders'),
]
