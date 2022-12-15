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
@user_passes_test(is_operator)
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
def Calendar(request):
    template_name= 'back/calendar.html'
    context = {
        'title': 'ini halaman Kalender'
    }
    return render(request, template_name, context)
