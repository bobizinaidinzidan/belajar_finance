from django.urls import path
from pengguna.views import TabelOperator, DeleteOperator, TabelUser, InputUser, EditUser, DeleteUser
#
urlpatterns = [
    # Halaman Tabel Operator
    path('operator/', TabelOperator, name='operator'), 
    #path('operator/edit-<str:id>', EditOperator, name='edit_operator'),
    path('operator/delete-<str:id>', DeleteOperator, name='delete_operator'),

    # Halaman Tabel User
    path('user/', TabelUser, name='user'), 
    #path('user/tambah',InputUser, name='tambah_user'),
    path('user/edit-<str:id>', EditUser, name='edit_user'),
    path('user/delete-<str:id>', DeleteUser, name='delete_user'),
]