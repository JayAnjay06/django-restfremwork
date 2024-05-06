from django.db import models

class Produk(models.Model):
    nama = models.CharField(max_length=200)
    deskripsi = models.TextField()
    harga = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nama

class Pelanggan(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    alamat = models.CharField(max_length=200)

    def __str__(self):
        return self.nama

class Pesan(models.Model):
    produk = models.ForeignKey(Produk, on_delete=models.CASCADE, related_name='Pesan_produk')
    pelanggan = models.ForeignKey(Pelanggan, on_delete=models.CASCADE, related_name='Pesan_pelanggan')
    jumlah = models.IntegerField()
    tanggal_Pesan = models.DateField()

    def __str__(self):
        return f"{self.pelanggan.nama} - {self.produk.nama}"