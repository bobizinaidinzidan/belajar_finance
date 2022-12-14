from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

from reksadana.models import *

import requests
# Create your views here.

def is_operator(user):
    if user.groups.filter(name='Operator').exists():
        return True
    else:
        return False

@user_passes_test(is_operator)
@login_required
def TabelReksadana(request):
    list_reksadana = TReksadana.objects.all()

    template_name = 'back/Tabel_reksadana/Treksadana.html'
    context = {
        'title' : 'ini Halaman Tabel Teksadana',
        'reksadana' : list_reksadana
    }
    return render(request, template_name, context)

@user_passes_test(is_operator)
@login_required
def DeleteReksadana(request, id):
    get_type = TReksadana.objects.get(id=id)
    get_type.delete()
    return redirect(TabelReksadana)

@user_passes_test(is_operator)
@login_required
def InputReksadana(request):
    template_name= 'back/Tabel_reksadana/Input_reksadana.html'
    if request.method == "POST":
        input_nama = request.POST.get('name')
        input_manajer = request.POST.get('manajer')
        input_bank_custodian = request.POST.get('custodian')
        input_jenis_reksa = request.POST.get('jenis_reksa')
        
        TReksadana.objects.create(
            name = input_nama,
            management = input_manajer,
            custodian = input_bank_custodian,
            tipe_reksadana = input_jenis_reksa,
        )
        return redirect(TabelReksadana)
    context= {
        'title' : 'ini halaman Input Reksadana',
    }
    return render(request, template_name, context)


@user_passes_test(is_operator)
@login_required
def EditReksadana(request, id):
    template_name = 'back/Tabel_reksadana/Edit_reksadana.html'
    get_reksadana = TReksadana.objects.get(id=id)
    
    if request.method == 'POST':
        input_nama = request.POST.get('name')
        input_manajer = request.POST.get('manajer')
        input_bank_custodian = request.POST.get('custodian')
        input_jenis_reksa = request.POST.get('jenis_reksa')
        
        
        # Bagian Mengedit Data
        get_reksadana.name = input_nama
        get_reksadana.management = input_manajer
        get_reksadana.custodian = input_bank_custodian
        get_reksadana.tipe_reksadana = input_jenis_reksa
        get_reksadana.save()
        
        print("Update/Edit Data")
    
        return redirect(TabelReksadana)
    context = {
        'title' : 'Ini Halaman Edit Data reksadana',
        'reksadana' : get_reksadana,
    }
    return render(request, template_name, context)


# Mengambila data dan melakukan singkron data    
@user_passes_test(is_operator)
@login_required
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