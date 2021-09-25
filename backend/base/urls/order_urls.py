from django.urls import path
from rest_framework import views
from ..views import order_views as views

urlpatterns = [
    path('add/',views.addOrderItems, name='order-add'),
    path('<str:pk>/',views.getOrderById, name='user-order'),
    path('<str:pk>/pay/',views.updateOrderToPaid, name='pay'),
    
    
]