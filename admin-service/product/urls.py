from django.urls import path
from product import views

urlpatterns = [
    path('products', views.ProductView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('products/<int:pk>', views.ProductView.as_view({
        'get': 'retrieve',
        'patch': 'update',
        'delete': 'destroy'
    })),
    path('users', views.UserAPIView.as_view())
]