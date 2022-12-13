from django.contrib import admin
from reksadana.models import *
 #Register your models here.
class ReksadanaAdmin(admin.ModelAdmin):
    list_display = ['name', 'management', 'custodian', 'tipe_reksadana']

admin.site.register(TReksadana, ReksadanaAdmin)
