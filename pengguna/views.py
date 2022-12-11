from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib.auth.models import User, Group

# Bagian User Pass test
def is_operator(user):
    if user.groups.filter(name='Operator').exists():
        return True
    else:
        return False


@login_required
# Bagian Tabel Operator
def TabelOperator(request):
    if request.user.groups.filter(name='Operator').exists():
        request.session['is_operator'] = 'operator'

    template_name= 'back/Tabel_operator/TOperator.html'
    list_user = User.objects.all()
    context = {
        'title': 'ini halaman Tabel Operator',
        'user': list_user,
    }
    return render(request, template_name, context)

@user_passes_test(is_operator)
@login_required
def InputOperator(request):
    template_name= 'back/Tabel_operator/Input_operator.html'
    list_group = Group.objects.all()
    if request.method == "POST":
        input_username = request.POST.get('username')
        input_password = request.POST.get('password')
        input_email = request.POST.get('email')
        #input_group = request.POST.get('group')
        input_first = request.POST.get('first_name')
        input_last = request.POST.get('last_name')

        #get_group = Group.objects.get(name=input_group)

        User.objects.create(
            username = input_username,
            password = input_password,
            email = input_email,
            #groups = get_group,
            first_name = input_first,
            last_name = input_last,
        )
        return redirect('operator')
    context= {
        'title' : 'ini halaman Input Buku',
        'group': list_group
    }
    return render(request, template_name, context)

@user_passes_test(is_operator)
@login_required
def EditOperator(request, id):
    template_name = 'back/Tabel_operator/Edit_operator.html'
    list_user = User.objects.get(id=id)
    
    if request.method == 'POST':
        input_penulis = request.POST.get('penulis')
        input_jenis_buku = request.POST.get('jenis_buku')
        input_judul = request.POST.get('judul')
        input_sinopsis = request.POST.get('sinopsis')
        input_penerbit = request.POST.get('penerbit')
        input_tanggal_terbit = request.POST.get('tanggal_terbit')
        
        get_penulis = Penulis.objects.get(nama=input_penulis)
        get_jenis_buku = Jenis.objects.get(nama=input_jenis_buku)

        # Bagian Mengedit Data
        list_user.penulis = get_penulis
        get_buku.jenis_buku = get_jenis_buku
        get_buku.judul = input_judul
        get_buku.sinopsis = input_sinopsis
        get_buku.penerbit = input_penerbit
        get_buku.date = input_tanggal_terbit
        get_buku.save()
        
        print("Update/Edit Data")
    
        return redirect(TabelBuku)
    context = {
        'title' : 'Ini Halaman Edit Data Buku',
        'user' : list_user,
    }
    return render(request, template_name, context)

@user_passes_test(is_operator)
@login_required
def DeleteOperator(request, id):
    get_user = User.objects.get(id=id)
    get_user.delete()
    return redirect('operator')


@user_passes_test(is_operator)
@login_required
# Bagian Tabel Admin
def TabelAdmin(request):
    template_name= 'back/Tabel_admin/TAdmin.html'
    context = {
        'title': 'ini halaman Tabel Admin',
    }
    return render(request, template_name, context)