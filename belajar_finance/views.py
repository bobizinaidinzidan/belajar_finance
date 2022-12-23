from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password
from pengguna.models import *

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

def Contact(request):
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

def Berita(request):
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
    if request.user.groups.filter(name='Operator').exists():
        request.session['is_operator'] = 'operator'

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

def Watchlist(request):
    if request.user.is_anonymous:
        print("Login Dahulu")
        list_reksadana = TReksadana.objects.all()
        list_watchlist = TWatchlist.objects.all()
    else:
        get_user = request.user
        
        list_reksadana = TReksadana.objects.all()
        list_watchlist = TWatchlist.objects.filter(id_user=get_user)
        for i in list_reksadana:
            for index in list_watchlist:
                if index.id_reksadana == i.id:
                    print('Berhasil')
    show_reksa = 10
    if request.GET:
        entry_data = request.GET.get('tambah_entry')
        show_reksa = int(entry_data)

    template_name = 'front/watchlist.html'
    context = {
            'title': 'Halaman Watchlist',
            'watchlist': list_watchlist,
            'reksadana': list_reksadana,
            'show': show_reksa,
        } 
    return render(request, template_name, context)    

def TambahWatchlist(request, id):
    get_user = request.user
    get_reksadana = TReksadana.objects.get(id=id)
    find_user = TWatchlist.objects.filter(id_user=get_user)
    find_reksadana = TWatchlist.objects.filter(id_reksadana=id)
    if find_user.exists():    
        for index in find_user:
            if str(index.id_reksadana) == id:
                update_watchlist = find_user.first()
                update_watchlist.id_user = get_user
                update_watchlist.id_reksadana = get_reksadana
                update_watchlist.save()  
        return addWatchlist(get_user, get_reksadana)          
    else:
        TWatchlist.objects.create(
            id_user=get_user,
            id_reksadana=get_reksadana,
        )    
def DeleteWatchlist(request, id):
    get_watchlist = TWatchlist.objects.get(id=id)
    get_watchlist.delete()       
    return redirect(Watchlist) 
    
    return redirect('reksadana')
def addWatchlist(data_user, data_id_reksa):
    TWatchlist.objects.create(
            id_user=data_user,
            id_reksadana=data_id_reksa,
        )  
    return redirect('watchlist')

# Bagian Login & Registrasi
def Login(request):
    if request.user.is_authenticated:
        return redirect('index')
    template_name = 'back/Login-Register/login.html'
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
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
    if request.POST:
        input_username = request.POST.get('username')
        input_password = request.POST.get('password')
        input_firstname = request.POST.get('first_name')
        input_lastname = request.POST.get('last_name')
        input_email = request.POST.get('in_email')
        #try:
        User.objects.create(
            username = input_username,
            password = make_password(input_password),
            first_name = input_firstname,
            last_name = input_lastname,
            email = input_email,
            is_staff = True,
        )
        get_user = User.objects.get(username=input_username)
        get_group = TGroup.objects.get(name="User")
        TAccount.objects.create(
            user = get_user,
            group = get_group
        )
        return redirect(index)
        #except:
            #pass
        
        #print(input_username, input_password, input_firstname, input_lastname, input_email)
    template_name = 'back/Login-Register/register.html'
    context = {
        'title' : 'Ini Halaman Register'
    }
    return render(request, template_name, context)