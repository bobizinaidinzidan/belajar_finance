from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib.auth.models import User, Group
from .models import *
# Bagian User Pass test
def is_operator(user):
    if user.groups.filter(name='Operator').exists():
        return True
    else:
        return False

# Bagian Tabel User
@user_passes_test(is_operator)
@login_required
def TabelAccount(request):
    list_account = TAccount.objects.all()
    template_name= 'back/Tabel_account/TAccount.html'
    list_user = User.objects.all()
    context = {
        'title': 'ini halaman Tabel Operator',
        'account': list_account
    }
    return render(request, template_name, context)

@user_passes_test(is_operator)
@login_required
def EditAccount(request, id):
    list_account = TAccount.objects.get(id=id)
    all_group = TGroup.objects.all()
    template_name= 'back/Tabel_account/Edit_account.html'
    if request.method == "POST":
        input_username = request.POST.get('username')
        input_group = request.POST.get('group')
        
        get_group = TGroup.objects.get(name=input_group)
        print(input_group)
        list_account.list_group = get_group
        list_account.save()
        return redirect('account')
    context= {
        'title' : 'ini halaman Input Account',
        'account': list_account,
        'group' : all_group
    }
    return render(request, template_name, context)

@user_passes_test(is_operator)
@login_required
def DeleteAccount(request, id):
    get_user = TAccount.objects.get(id=id)
    print(get_user)
    get_user.delete()
    return redirect('account')
