from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'produk', views.ProdukViewSet)
router.register(r'pelanggan', views.PelangganViewSet)
router.register(r'penjualan', views.PesanViewSet)

urlpatterns = router.urls
