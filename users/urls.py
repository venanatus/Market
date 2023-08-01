from django.urls import path
from . import views

urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_in/', views.a, name='a'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.out, name='logout'),
    path('create_profile/', views.create_profile, name='create_profile')
]
