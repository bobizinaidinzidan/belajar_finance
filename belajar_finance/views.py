from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, user_passes_test

from buku.models import *

# Bagian User Pass test
def is_operator(user):
    if user.groups.filter(name='Operator').exists():
        return True
    elif user.groups.filter(name='User').exist():
        return True
    else:
        return False

# bagian Front end
def index(request):
    if request.user.groups.filter(name='Operator').exists():
        request.session['is_operator'] = 'operator'
    elif request.user.groups.filter(name='User').exists():
        request.session['is_operator'] = 'user'

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

@login_required
def account(request):
    template_name = 'front/account.html'
    context = {
        'title' : 'ini halaman Akun'
    }
    return render(request, template_name, context)
def postingan(request):
    template_name = 'front/blog-post.html'
    context = {
        'title': 'Ini Halman Postingan'
    }
    return render(request, template_name, context)

def berita(request):
    template_name = 'front/blog-posts.html'
    context = {
        'title': 'Ini Halman berita'
    }
    return render(request, template_name, context)

def Reksadana(request):
    template_name = 'front/reksadana.html'
    context = {
        'title' : 'Ini Halaman Register'
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
def Lock(request):
    template_name = 'back/Login-Register/lock.html'
    context = {
        'title' : 'Ini Halaman Lock'
    }
    return render(request, template_name, context)

