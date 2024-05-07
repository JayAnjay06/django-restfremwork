from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('produk/', views.produk_list),
    path('produk/<int:pk>/', views.produk_detail),
    path('pelanggan/', views.pelanggan_list),
    path('pelanggan/<int:pk>/', views.pelanggan_detail),
    path('pesan/', views.pesan_list),
    path('pesan/<int:pk>/', views.pesan_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)