from django.urls import path, include
from buku.views import dashboard, Calendar, TabelBuku, InputBuku, LihatBuku, EditBuku, DeleteBuku

urlpatterns = [
    path('', include('pengguna.urls')),

    # halaman Nav Dashboard(back end)
    path('', dashboard, name='dashboard'),
    path('calendar/', Calendar, name='calendar'),
    
    # Halaman Tabel Buku
    path('buku/', TabelBuku, name='Tbuku'),
    path('buku/tambah', InputBuku, name='input_buku'),
    path('buku/lihat-<str:id>', LihatBuku, name='lihat_buku'),
    path('buku/edit-<str:id>', EditBuku, name='edit_buku'),
    path('buku/delete-<str:id>', DeleteBuku, name='delete_buku'),
]   