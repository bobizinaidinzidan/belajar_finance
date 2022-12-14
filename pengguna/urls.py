from django.urls import path
from pengguna.views import TabelOperator, EditOperator, DeleteOperator, TabelUser,DeleteUser

urlpatterns = [
    # Halaman Tabel Operator
    path('operator/', TabelOperator, name='operator'), 
    path('operator/edit-<str:id>', EditOperator, name='edit_operator'),
    path('operator/delete-<str:id>', DeleteOperator, name='delete_operator'),

    # Halaman Tabel User
    path('user/', TabelUser, name='user'), 
    #path('operator/edit-<str:id>', EditOperator, name='edit_operator'),
    path('user/delete-<str:id>', DeleteUser, name='delete_user'),
]