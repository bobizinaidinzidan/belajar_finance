from django.contrib import admin
from buku.models import *
# Register your models here.
class BukuAdmin(admin.ModelAdmin):
    list_display = ['penulis', 'jenis_buku', 'judul', 'penerbit', 'date', 'sinopsis']

admin.site.register(Buku, BukuAdmin)
