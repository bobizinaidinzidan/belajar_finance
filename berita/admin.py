from django.contrib import admin
from berita.models import *
 #Register your models here.
class BeritaAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'tags','description', 'url', 'urlToImage', 'publishedAt']

admin.site.register(TBerita, BeritaAdmin)
