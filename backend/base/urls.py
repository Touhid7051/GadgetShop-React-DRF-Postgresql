from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('',views.getRoute, name="routes"),
    path('users/profile/',views.getUserProfile, name="users-profile"),
    path('products/',views.getProducts, name="products"),
    path('products/<str:pk>',views.getProduct, name="products"),
    
]