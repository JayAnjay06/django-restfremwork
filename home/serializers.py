from rest_framework import serializers
from .models import *

class PelangganSerializers(serializers.ModelSerializer):
    class Meta :
        model  = Pelanggan
        fields = {"id" , "nama", "email", "address"}