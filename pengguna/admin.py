from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(TGroup)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'group']

admin.site.register(TAccount, AccountAdmin)
