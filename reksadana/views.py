from django.shortcuts import render, HttpResponse, redirect
from reksadana.models import *

import requests
# Create your views here.

def TabelReksadana(request):
    list_reksadana = TReksadana.objects.all()

    template_name = 'back/Tabel_reksadana/Treksadana.html'
    context = {
        'title' : 'ini Halaman Tabel Teksadana',
        'reksadana' : list_reksadana
    }
    return render(request, template_name, context)
def DeleteReksadana(request, id):
    get_type = TReksadana.objects.get(id=id)
    get_type.delete()
    return redirect(TabelReksadana)


# Mengambila data dan melakukan singkron data    

def SingkronDataReksdana(request):
    x = requests.get('https://ojk-invest-api.vercel.app/api/products')
    data = x.json()    #print the response text (the content of the requested file):
    loop = data['data']         
    for i in loop["products"]:
        name_reksa = i['name']
        management_reksa = i['management']
        custodian_reksa = i['custodian']
        type_reksa = i['type']

        reksadana_list = TReksadana.objects.filter(name=name_reksa)

        if reksadana_list.exists():
             reksadana_update = reksadana_list.first()
             reksadana_update.name = name_reksa
             reksadana_update.management = management_reksa
             reksadana_update.custodian = custodian_reksa
             reksadana_update.tipe_reksadana = type_reksa
             reksadana_update.save()

        else :
            TReksadana.objects.create(
                name = name_reksa,
                management = management_reksa,
                custodian = custodian_reksa,
                tipe_reksadana =type_reksa,
            )
    return redirect(TabelReksadana)