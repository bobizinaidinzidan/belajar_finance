from django.urls import path
from reksadana.views import TabelReksadana, SingkronData

urlpatterns = [
    
    # Halaman Tabel Buku
    path('reksadana/', TabelReksadana, name='Treksadana'),
    path('reksadana/singkron', SingkronData, name='singkron_data'),
    #path('buku/lihat-<str:id>', LihatBuku, name='lihat_buku'),
    #path('buku/edit-<str:id>', EditBuku, name='edit_buku'),
    #path('buku/delete-<str:id>', DeleteBuku, name='delete_buku'),
]