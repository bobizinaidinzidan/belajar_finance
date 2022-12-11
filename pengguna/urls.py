from django.urls import path
from pengguna.views import TabelOperator, InputOperator, EditOperator, DeleteOperator, TabelAdmin 

urlpatterns = [
    # Halaman Tabel Operator
    path('operator/', TabelOperator, name='operator'), 
    path('operator/tambah', InputOperator, name='input_operator'),
    path('operator/edit-<str:id>', EditOperator, name='edit_operator'),
    path('operator/delete-<str:id>', DeleteOperator, name='delete_operator'),


    # Halaman Tabel Admin
    path('admin/', TabelAdmin, name='admin'),
]