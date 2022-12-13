from django.urls import path
from reksadana.views import TabelReksadana, DeleteReksadana, SingkronDataReksdana

urlpatterns = [
    
    # Halaman Tabel Buku
    path('reksadana/', TabelReksadana, name='Treksadana'),
    path('reksadana/singkron-ReksadanaAPI', SingkronDataReksdana, name='singkron_data_reksadana'),
    #path('buku/lihat-<str:id>', LihatBuku, name='lihat_buku'),
    #path('buku/edit-<str:id>', EditBuku, name='edit_buku'),
    path('reksadana/delete-<str:id>', DeleteReksadana, name='delete_reksa'),
]