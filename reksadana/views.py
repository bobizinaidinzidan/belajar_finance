from django.shortcuts import render, HttpResponse, redirect
from reksadana.models import *
#import requests
# Create your views here.

def TabelReksadana(request):
    list_reksadana = Reksadana.objects.all()

    template_name = 'back/Tabel_reksadana/Treksadana.html'
    context = {
        'title' : 'ini Halaman Tabel Teksadana',
        'reksadana' : list_reksadana
    }
    return render(request, template_name, context)

def SingkronData(request):    
    template_name = 'back/Tabel_reksadana/text.html'
   # list_test = requests.get('https://api.covid19api.com/countries').json()

    context = {
        'title' : 'ini Halaman Tabel Teksadana',
        'test': list_test
    }
    return render(request, template_name, context)

