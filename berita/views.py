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
def InputBerita(request):
    template_name= 'back/Tabel_berita/Input_berita.html'
    if request.method == "POST":
        input_author = request.POST.get('author')
        input_title = request.POST.get('title')
        input_tags = request.POST.get('tags')
        input_description = request.POST.get('description')
        input_url = request.POST.get('url_readmore')
        input_urlToImage = request.POST.get('url_image')
        input_publishedAt = request.POST.get('publishedAt')
        
        TBerita.objects.create(
            author = input_author,
            title = input_title,
            tags = input_tags,
            description = input_description,
            url = input_url,
            urlToImage = input_urlToImage,
            publishedAt = input_publishedAt,
        )
        return redirect(TabelBerita)
    context= {
        'title' : 'ini halaman Input Reksadana',
    }
    return render(request, template_name, context)

@user_passes_test(is_operator)
@login_required
def EditBerita(request, id):
    template_name = 'back/Tabel_berita/Edit_berita.html'
    get_berita = TBerita.objects.get(id=id)
    
    if request.method == 'POST':
        input_author = request.POST.get('author')
        input_title = request.POST.get('title')
        input_tags = request.POST.get('tags')
        input_description = request.POST.get('description')
        input_url = request.POST.get('url_readmore')
        input_urlToImage = request.POST.get('url_image')
        input_publishedAt = request.POST.get('publishedAt')
        
        # Bagian Mengedit Data
        get_berita.author = input_author
        get_berita.title = input_title
        get_berita.tags = input_tags
        get_berita.description = input_description
        get_berita.url = input_url
        get_berita.urlToImage = input_urlToImage
        get_berita.publishedAt = input_publishedAt
        get_berita.save()
        
        print("Update/Edit Data")
    
        return redirect(TabelBerita)
    context = {
        'title' : 'Ini Halaman Edit Data reksadana',
        'berita' : get_berita,
    }
    return render(request, template_name, context)

@user_passes_test(is_operator)
@login_required
def DeleteBerita(request, id):
    get_berita = TBerita.objects.get(id=id)
    get_berita.delete()
    return redirect(TabelBerita)

# Mengambila data dan melakukan singkron data    
@user_passes_test(is_operator)
@login_required
def SingkronDataBerita(request):
    api = requests.get('https://berita-indo-api.vercel.app/v1/cnbc-news/investment')
    data = api.json()

    for i in data['data']:
        author_berita = "CNBC News"
        title_berita = i['title']
        describtion_berita = i['contentSnippet']
        url_berita = i['link']
        urlToImage_berita = i['image']['large']
        if urlToImage_berita == "":
            urlToImage_berita = i['image']['small']
        publishhedAt_berita = i['isoDate']
        get_berita = "Investment"
        berita_list = TBerita.objects.filter(title=title_berita)
        if berita_list.exists():
            berita_update = berita_list.first()
            berita_update.author = author_berita
            berita_update.title = title_berita
            berita_update.tags = get_berita
            berita_update.description = describtion_berita
            berita_update.url = url_berita
            berita_update.urlToImage = urlToImage_berita
            berita_update.publishedAt = publishhedAt_berita
            berita_update.save()
        else :
            TBerita.objects.create(
                author = author_berita,
                title = title_berita,
                tags = get_berita,
                description = describtion_berita,
                url = url_berita,
                urlToImage = urlToImage_berita,
                publishedAt = publishhedAt_berita,
            )
    
    return redirect(TabelBerita)