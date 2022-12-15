from django.urls import path, include
from buku.views import dashboard, Calendar
urlpatterns = [
    path('', include('pengguna.urls')),

    # halaman Nav Dashboard(back end)
    path('', dashboard, name='dashboard'),
    path('calendar/', Calendar, name='calendar'),
]   