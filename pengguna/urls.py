from django.urls import path
from pengguna.views import Dashboard, Calendar, TabelAccount, EditAccount, DeleteAccount

urlpatterns = [
    # halaman Nav Dashboard(back end)
    path('', Dashboard, name='dashboard'),
    path('calendar/', Calendar, name='calendar'),

    # Halaman Tabel Account
    path('account/', TabelAccount, name='account'), 
    path('account/delete-<str:id>', DeleteAccount, name='delete_account'),
    path('account/edit-<str:id>', EditAccount, name='edit_account'),
]