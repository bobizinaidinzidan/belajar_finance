from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, user_passes_test

from reksadana.models import *
from berita.models import *
# Bagian User Pass test
def is_operator(user):
    if user.groups.filter(name='Operator').exists():
        return True
    else:
        return False

# bagian Front end
def index(request):
    if request.user.groups.filter(name='Operator').exists():
        request.session['is_operator'] = 'operator'

    template_name = 'front/index.html'

    context = {
        'title': 'ini halaman Home',
    }
    return render(request, template_name, context)

def contact(request):
    template_name = 'front/contact-us.html'
    context = {
        'title': 'Ini Halman Home'
    }
    return render(request, template_name, context)

def postingan(request):
    template_name = 'front/postingan.html'
    context = {
        'title': 'Ini Halman Postingan'
    }
    return render(request, template_name, context)

def berita(request):
    template_name = 'front/berita.html'
    list_berita = TBerita.objects.all()
    show_berita = 10
    if request.GET:
        entry_data = request.GET.get('tambah_entry')
        show_berita = int(entry_data) # Jumlah data yang tampil
    
    context = {
        'title': 'Ini Halman berita',
        'berita': list_berita,
        'show': show_berita
    }
    return render(request, template_name, context)

def Reksadana(request):
    list_reksadana1 = TReksadana.objects.filter(tipe_reksadana="Fixed Income Fund")
    list_reksadana2 = TReksadana.objects.filter(tipe_reksadana="Money Market Fund")
    list_reksadana3 = TReksadana.objects.filter(tipe_reksadana="Mixed Asset Fund")
    list_reksadana4 = TReksadana.objects.filter(tipe_reksadana="RD - Saham")
    show_reksa = 10
    if request.GET:
        entry_data = request.GET.get('tambah_entry')
        show_reksa = int(entry_data) 
    template_name = 'front/reksadana.html'
    context = {
        'title' : 'Ini Halaman Register',
        'reksadana1' : list_reksadana1,
        'reksadana2' : list_reksadana2,
        'reksadana3' : list_reksadana3,
        'reksadana4' : list_reksadana4,
        'show': show_reksa
    }
    return render(request, template_name, context)


# Bagian Login & Registrasi

def Login(request):
    if request.user.is_authenticated:
        return redirect('index')
    template_name = 'back/Login-Register/login.html'
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('Username: ', username, 'Password: ',password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Data ada
            auth_login(request, user)
            return redirect('index')
            pass
        else:
            # Data tidak ada
            return redirect('login')
            pass

    context = {
        'title' : 'Ini Halaman Login'
    }
    return render(request, template_name, context)
def Logout(request):
    logout(request)
    return redirect('login')  

def Register(request):
    template_name = 'back/Login-Register/register.html'
    context = {
        'title' : 'Ini Halaman Register'
    }
    return render(request, template_name, context)