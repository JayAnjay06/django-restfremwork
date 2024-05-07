from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

@api_view(['GET', 'POST'])
def produk_list(request):
    if request.method == 'GET':
        produks = Produk.objects.all()
        serializer = ProdukSerializer(produks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProdukSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def produk_detail(request, pk):
    try:
        produk = produk.objects.get(pk=pk)
    except produk.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProdukSerializer(produk)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProdukSerializer(produk, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        produk.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def pelanggan_list(request):
    if request.method == 'GET':
        pelanggans= Pelanggan.objects.all()
        serializer = PelangganSerializer(pelanggans, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PelangganSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def pelanggan_detail(request, pk):
    try:
        pelanggan = pelanggan.objects.get(pk=pk)
    except pelanggan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PelangganSerializer(pelanggan)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PelangganSerializer(pelanggan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        pelanggan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def pesan_list(request):
    if request.method == 'GET':
        pesans= Pesan.objects.all()
        serializer = PesanSerializer(pesans, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PesanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def pesan_detail(request, pk):
    try:
        pesan = pesan.objects.get(pk=pk)
    except pesan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PesanSerializer(pesan)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PesanSerializer(pesan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        pesan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)