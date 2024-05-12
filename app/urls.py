from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('produk/', views.ProdukList.as_view()),
    path('produk/<int:pk>/', views.ProdukDetail.as_view()),
    path('pelanggan/', views.PelangganList.as_view()),
    path('pelanggan/<int:pk>/', views.PelangganDetail.as_view()),
    path('pesan/', views.PesanList.as_view()),
    path('pesan/<int:pk>/', views.PesanDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)