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

from . views import index, contact, Reksadana, berita, postingan, Login, Logout, Register

urlpatterns = [
    path('admin/', admin.site.urls),

    # halaman front end
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('berita/', berita, name='berita'),
    path('postingan/', postingan, name='postingan'),
    path('reksadana/', Reksadana, name='reksadana'),

    # halaman Tabel buku
    path('dashboard/', include('buku.urls')),

    # halaman Tabel berita
    path('dashboard/', include('berita.urls')),

    # halaman Tabel reksadana 
    path('dashboard/', include('reksadana.urls')),
    
    # Halaman Login Logout
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('register/', Register, name='register'),
]    