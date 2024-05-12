from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

class ProdukList(APIView):
    def get(self, request, format=None):
        produk = Produk.objects.all()
        serializer = ProdukSerializer(produk, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProdukSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProdukDetail(APIView):
    def get_object(self, pk):
        try:
            return Produk.objects.get(pk=pk)
        except Produk.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        produk = self.get_object(pk)
        serializer = ProdukSerializer(produk)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        produk = self.get_object(pk)
        serializer = ProdukSerializer(produk, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        produk = self.get_object(pk)
        produk.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class PelangganList(APIView):
    def get(self, request, format=None):
        pelanggan = Pelanggan.objects.all()
        serializer = PelangganSerializer(pelanggan, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PelangganSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PelangganDetail(APIView):
    def get_object(self, pk):
        try:
            return Pelanggan.objects.get(pk=pk)
        except Pelanggan.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pelanggan = self.get_object(pk)
        serializer = PelangganSerializer(pelanggan)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        pelanggan = self.get_object(pk)
        serializer = PelangganSerializer(pelanggan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pelanggan = self.get_object(pk)
        pelanggan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class PesanList(APIView):
    def get(self, request, format=None):
        pesan = Pesan.objects.all()
        serializer = PesanSerializer(pesan, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PesanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PesanDetail(APIView):
    def get_object(self, pk):
        try:
            return Pesan.objects.get(pk=pk)
        except Pesan.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pesan = self.get_object(pk)
        serializer = PesanSerializer(pesan)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        pesan = self.get_object(pk)
        serializer = PesanSerializer(pesan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pesan = self.get_object(pk)
        pesan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)