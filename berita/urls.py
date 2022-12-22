from django.urls import path
from berita.views import TabelBerita, DeleteBerita, InputBerita, EditBerita, SingkronDataBerita

urlpatterns = [
    path('berita', TabelBerita, name='Tberita'),
    path('berita/tambah', InputBerita, name='tambah_berita'),
    path('berita/edit-<str:id>', EditBerita, name='edit_berita'),
    path('berita/hapus-<str:id>', DeleteBerita, name='delete_berita'),

    # Singkronisasi Data API Berita
    path('berita/singkron_BeritaAPI', SingkronDataBerita, name='singkrondataberita'),
]