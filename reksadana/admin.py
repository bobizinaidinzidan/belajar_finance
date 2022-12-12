from django.contrib import admin
from reksadana.models import *
# Register your models here.
admin.site.register(Type)
class ReksadanaAdmin(admin.ModelAdmin):
    list_display = ['name', 'management', 'custodian', 'type']

admin.site.register(TReksadana, ReksadanaAdmin)
