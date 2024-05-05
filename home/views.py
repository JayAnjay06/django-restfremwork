from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

@api_view()
def home(request):
    return Response({'status' : 200 , 'message' : 'hello from django rest framework'})

class PelangganViewset(viewsets.ModelViewSet):
    queryset = Pelanggan.objects.all()
    serializer_class = PelangganSerializers