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
def DeleteData(request, id):
    get_type = Type.objects.get(id=id)
    get_type.delete()
    return redirect(TabelReksadana)


# Mengambila data dan melakukan singkron data    
def SingkronDataTypeReksa(request):
    x = requests.get('https://ojk-invest-api.vercel.app/api/products')
    data = x.json()    #print the response text (the content of the requested file):
    loop = data['data']         
    for i in loop["products"]:
        type_reksa = i['type']
        
        get_reksa = Type.objects.filter(name=type_reksa)
        if get_reksa.exists():
            jenis_reksa = get_reksa.first()
            jenis_reksa.name = type_reksa        
            jenis_reksa.save() 
       
        else: 
            Type.objects.create(
                name = type_reksa,
            ) 
             
    return redirect(TabelReksadana)

def SingkronDataReksdana(request):
    x = requests.get('https://ojk-invest-api.vercel.app/api/products')
    data = x.json()    #print the response text (the content of the requested file):
    loop = data['data']         
    for i in loop["products"]:
        name_reksa = i['name']
        management_reksa = i['management']
        custodian_reksa = i['custodian']
        type_reksa = i['type']

        jenis_reksa = Type.objects.get(name=type_reksa)
        
        if type_reksa == "Money Market Fund":
            TReksadana.objects.create(
                name = name_reksa,
                management = management_reksa,
                custodian = custodian_reksa,
                type =jenis_reksa,
            ) 
        elif type_reksa == "Mixed Asset Fund":
            TReksadana.objects.create(
                name = name_reksa,
                management = management_reksa,
                custodian = custodian_reksa,
                type =jenis_reksa,
            ) 
        elif type_reksa == "Fixed Income Fund":
            TReksadana.objects.create(
                name = name_reksa,
                management = management_reksa,
                custodian = custodian_reksa,
                type =jenis_reksa,
            ) 
        elif type_reksa == "RD - Saham":
            TReksadana.objects.create(
                name = name_reksa,
                management = management_reksa,
                custodian = custodian_reksa,
                type =jenis_reksa,
            ) 
        else :
            print("Data Tidak sesuai!!!")
    return redirect(TabelReksadana)