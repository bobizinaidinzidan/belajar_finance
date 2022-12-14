from django.contrib import admin
from berita.models import *
 #Register your models here.
admin.site.register(TypeBerita)
class BeritaAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'tipe_berita','description', 'url', 'urlToImage', 'publishedAt', 'content']

admin.site.register(TBerita, BeritaAdmin)
