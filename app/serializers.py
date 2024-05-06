from rest_framework import serializers
from .models import *

class ProdukSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produk
        fields = '__all__'

class PelangganSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelanggan
        fields = '__all__'

class PesanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesan
        fields = '__all__'