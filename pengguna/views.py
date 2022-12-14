from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib.auth.models import User, Group

# Bagian User Pass test
def is_operator(user):
    if user.groups.filter(name='Operator').exists():
        return True
    else:
        return False

@user_passes_test(is_operator)
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
def EditOperator(request):
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
def DeleteOperator(request, id):
    get_user = User.objects.get(id=id)
    get_user.delete()
    return redirect('operator')

@user_passes_test(is_operator)
@login_required
# Bagian Tabel Operator
def TabelUser(request):
    if request.user.groups.filter(name='Operator').exists():
        request.session['is_operator'] = 'operator'

    template_name= 'back/Tabel_user/TUser.html'
    list_user = User.objects.all()
    context = {
        'title': 'ini halaman Tabel Operator',
        'user': list_user,
    }
    return render(request, template_name, context)

@user_passes_test(is_operator)
@login_required
def DeleteUser(request, id):
    get_user = User.objects.get(id=id)
    get_user.delete()
    return redirect('user')
