from django.urls import path
from pengguna.views import TabelAccount, EditAccount, DeleteAccount
#
urlpatterns = [
    # Halaman Tabel Account
    path('account/', TabelAccount, name='account'), 
    path('account/delete-<str:id>', DeleteAccount, name='delete_account'),
    path('account/edit-<str:id>', EditAccount, name='edit_account'),
]