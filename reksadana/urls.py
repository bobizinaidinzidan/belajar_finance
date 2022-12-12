from django.urls import path
from reksadana.views import TabelReksadana, SingkronDataReksdana, SingkronDataTypeReksa

urlpatterns = [
    
    # Halaman Tabel Buku
    path('reksadana/', TabelReksadana, name='Treksadana'),
    path('reksadana/singkron-ReksadanaAPI', SingkronDataReksdana, name='singkron_data_reksadana'),
    path('reksadana/singkron-TypeReksaAPI', SingkronDataTypeReksa, name='singkron_data_type'),
    #path('buku/lihat-<str:id>', LihatBuku, name='lihat_buku'),
    #path('buku/edit-<str:id>', EditBuku, name='edit_buku'),
    #path('buku/delete-<str:id>', DeleteBuku, name='delete_buku'),
]