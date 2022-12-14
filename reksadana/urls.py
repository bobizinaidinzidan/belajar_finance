from django.urls import path
from reksadana.views import TabelReksadana, InputReksadana, EditReksadana, DeleteReksadana, SingkronDataReksdana

urlpatterns = [
    
    # Halaman Tabel Buku
    path('reksadana/', TabelReksadana, name='Treksadana'),
    path('reksadana/tambah', InputReksadana, name='tambah_reksadana'),
    path('reksadana/edit-<str:id>', EditReksadana, name='edit_reksa'),
    path('reksadana/delete-<str:id>', DeleteReksadana, name='delete_reksa'),
    path('reksadana/singkron-ReksadanaAPI', SingkronDataReksdana, name='singkron_data_reksadana'),
]