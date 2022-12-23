"""tugas_template URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . views import index, Contact, Reksadana, Berita, Watchlist, TambahWatchlist, DeleteWatchlist, postingan, Login, Logout, Register

urlpatterns = [
    path('admin/', admin.site.urls),

    # halaman front end
    path('', index, name='index'),
    path('contact/', Contact, name='contact'),
    path('berita/', Berita, name='berita'),
    path('postingan/', postingan, name='postingan'),
    path('reksadana/', Reksadana, name='reksadana'),
    path('watchlist/', Watchlist, name='watchlist'),
    path('watchlist_add-<str:id>', TambahWatchlist, name='add_watchlist'),
    path('watchlist_delete-<str:id>', DeleteWatchlist, name='delete_watchlist'),

    # halaman Tabel buku
    path('dashboard/', include('pengguna.urls')),

    # halaman Tabel berita
    path('dashboard/', include('berita.urls')),

    # halaman Tabel reksadana 
    path('dashboard/', include('reksadana.urls')),
    
    # Halaman Login Logout
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('register/', Register, name='register'),
]    