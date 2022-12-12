from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import *

# Bagian User Pass test
def is_operator(user):
    if user.groups.filter(name='Operator').exists():
        return True
    else:
        return False

#Bagian Nav Dashboard
@login_required
def dashboard(request):
    if request.user.groups.filter(name='Operator').exists():
        request.session['is_operator'] = 'operator'

    template_name= 'back/dashboard.html'
    context = {
        'title': 'ini halaman dashboard'
    }
    return render(request, template_name, context)

@login_required
def Charts(request):
    template_name= 'back/Charts.html'
    context = {
        'title': 'ini halaman Charts'
    }
    return render(request, template_name, context)

@login_required
def Calendar(request):
    template_name= 'back/calendar.html'
    context = {
        'title': 'ini halaman Kalender'
    }
    return render(request, template_name, context)

@login_required
def Widgets(request):
    template_name ='back/widgets.html'
    context = {
        'title' : 'Ini halaman Widgets'
    }
    return render(request, template_name, context)
    
@login_required
def User(request):
    template_name = 'back/Login-Register/user.html'
    context = {
        'title' : 'Ini Halaman User'
    }
    return render(request, template_name, context)

#Bagian Tabel Buku
@login_required
def TabelBuku(request):
    template_name= 'back/Tabel_buku/TBuku.html'
    list_buku = Buku.objects.all()
    
    context = {
        'title': 'ini halaman List Buku',
        'buku' : list_buku
    }
    return render(request, template_name, context)

@login_required
def InputBuku(request):
    template_name= 'back/Tabel_buku/Input_Buku.html'
    if request.method == "POST":
        input_penulis = request.POST.get('penulis')
        input_jenis_buku = request.POST.get('jenis_buku')
        input_judul = request.POST.get('judul')
        input_sinopsis = request.POST.get('sinopsis')
        input_penerbit = request.POST.get('penerbit')
        input_tanggal_terbit = request.POST.get('tanggal_terbit')

        Buku.objects.create(
            penulis = input_penulis,
            jenis_buku = input_jenis_buku,
            judul = input_judul,
            sinopsis = input_sinopsis,
            penerbit = input_penerbit,
            date = input_tanggal_terbit,
        )
        return redirect(TabelBuku)
    context= {
        'title' : 'ini halaman Input Buku',
    }
    return render(request, template_name, context)

@login_required
def LihatBuku(request, id):
    template_name = 'back/Tabel_buku/Lihat_Buku.html'
    list_buku = Buku.objects.get(id=id)
    context = {
        'title' : 'Ini Melihat datail Buku',
        'buku': list_buku
    }
    return render(request, template_name, context)

@login_required
def EditBuku(request, id):
    template_name = 'back/Tabel_buku/Edit_buku.html'
    get_buku = Buku.objects.get(id=id)
    
    if request.method == 'POST':
        input_penulis = request.POST.get('penulis')
        input_jenis_buku = request.POST.get('jenis_buku')
        input_judul = request.POST.get('judul')
        input_sinopsis = request.POST.get('sinopsis')
        input_penerbit = request.POST.get('penerbit')
        input_tanggal_terbit = request.POST.get('tanggal_terbit')

        # Bagian Mengedit Data
        get_buku.penulis = input_penulis
        get_buku.jenis_buku = input_jenis_buku
        get_buku.judul = input_judul
        get_buku.sinopsis = input_sinopsis
        get_buku.penerbit = input_penerbit
        get_buku.date = input_tanggal_terbit
        get_buku.save()
        
        print("Update/Edit Data")
    
        return redirect(TabelBuku)
    context = {
        'title' : 'Ini Halaman Edit Data Buku',
        'buku' : get_buku,
    }
    return render(request, template_name, context)

@login_required
def DeleteBuku(request, id):
    get_buku = Buku.objects.get(id=id)
    get_buku.delete()
    return redirect(TabelBuku)
