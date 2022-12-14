from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

from berita.models import *

import requests
# Create your views here.

def is_operator(user):
    if user.groups.filter(name='Operator').exists():
        return True
    else:
        return False

@user_passes_test(is_operator)
@login_required
def TabelBerita(request):
    list_berita = TBerita.objects.all()

    template_name = 'back/Tabel_berita/Tberita.html'
    context = {
        'title' : 'ini Halaman Tabel berita',
        'berita' : list_berita
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
def SingkronDataBerita(request):
    key = 'a178644808ab47108ea5c7394d41d9f7'
    api1 = requests.get(f'https://newsapi.org/v2/top-headlines?category=business&country=id&apiKey={key}')
    data1 = api1.json()

    for i in data1['articles']:
        author_berita = i['author']
        title_berita = i['title']
        describtion_berita = i['description']
        url_berita = i['url']
        urlToImage_berita = i['urlToImage']
        publishhedAt_berita = i['publishedAt']
        content_berita = i['content']

        berita_list = TBerita.objects.filter(title=title_berita)
        get_berita = TypeBerita.objects.get(name="Business")

        if berita_list.exists():
            berita_update = berita_list.first()
            berita_update.author = author_berita
            berita_update.title = title_berita
            berita_update.tipe_berita = get_berita
            berita_update.description = describtion_berita
            berita_update.url = url_berita
            berita_update.urlToImage = urlToImage_berita
            berita_update.publishedAt = publishhedAt_berita
            berita_update.content =content_berita
            berita_update.save()
        else :
            TBerita.objects.create(
                author = author_berita,
                title = title_berita,
                tipe_berita = get_berita,
                description = describtion_berita,
                url = url_berita,
                urlToImage = urlToImage_berita,
                publishedAt = publishhedAt_berita,
                content = content_berita,
            )
    
    api2 = requests.get('https://berita-indo-api.vercel.app/v1/cnbc-news/investment')
    data2 = api2.json()

    for i in data2['data']:
        author_berita = "CNBC News"
        title_berita = i['title']
        describtion_berita = i['contentSnippet']
        url_berita = i['link']
        urlToImage_berita = i['image']['large']
        publishhedAt_berita = i['isoDate']
        content_berita = ""

        berita_list = TBerita.objects.filter(title=title_berita)
        get_berita = TypeBerita.objects.get(name="Investment")

        if berita_list.exists():
            berita_update = berita_list.first()
            berita_update.author = author_berita
            berita_update.title = title_berita
            berita_update.tipe_berita = get_berita
            berita_update.description = describtion_berita
            berita_update.url = url_berita
            berita_update.urlToImage = urlToImage_berita
            berita_update.publishedAt = publishhedAt_berita
            berita_update.content =content_berita
            berita_update.save()
        else :
            TBerita.objects.create(
                author = author_berita,
                title = title_berita,
                tipe_berita = get_berita,
                description = describtion_berita,
                url = url_berita,
                urlToImage = urlToImage_berita,
                publishedAt = publishhedAt_berita,
                content = content_berita,
            )
    
    return redirect(TabelBerita)