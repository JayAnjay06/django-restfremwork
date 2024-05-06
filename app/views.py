from rest_framework import viewsets
from .models import *
from .serializers import *

class ProdukViewSet(viewsets.ModelViewSet):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer

class PelangganViewSet(viewsets.ModelViewSet):
    queryset = Pelanggan.objects.all()
    serializer_class = PelangganSerializer

class PesanViewSet(viewsets.ModelViewSet):
    queryset = Pesan.objects.all()
    serializer_class = PesanSerializer