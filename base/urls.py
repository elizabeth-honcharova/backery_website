from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('shop/', views.shop, name='shop'),
    path('item-details/<str:pk>/', views.item, name='item-details'),
    path('courses/', views.courses, name='courses'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart'),
    path('orders/', views.orders, name='orders'),
    path('delete-item/<str:pk>/', views.deleteCartItem, name='delete-item'),
]
