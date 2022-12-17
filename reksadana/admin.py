from django.contrib import admin
from reksadana.models import *
 #Register your models here.
class ReksadanaAdmin(admin.ModelAdmin):
    list_display = ['name', 'management', 'custodian', 'tipe_reksadana']

admin.site.register(TReksadana, ReksadanaAdmin)

class WatchlistAdmin(admin.ModelAdmin):
    list_display = ['id_user', 'id_reksadana']

admin.site.register(TWatchlist, WatchlistAdmin)
