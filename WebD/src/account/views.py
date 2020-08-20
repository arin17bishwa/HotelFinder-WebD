from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout

from .forms import (
    RegistrationForm,
    AccountAuthenticationForm,
    AccountUpdateForm,
)

from personal.models import Hotel

import json
# Create your views here.

def registration_view(request):
    context={}
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            account=authenticate(username=username,password=raw_password)
            login(request,account)
            return redirect('personal:home')
        else:
            context['registration_form']=form
    else:#it means it is a GET request
        form=RegistrationForm()
        context['registration_form'] = form
    return render(request,'account/register.html',context)


def logout_view(request):
    logout(request)
    return redirect('personal:home')

def login_view(request):
    context={}

    user=request.user
    if user.is_authenticated:
        return redirect('personal:home')

    if request.POST:
        form=AccountAuthenticationForm(request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=username,password=password)

            if user:
                login(request,user)
                return redirect('personal:home')
    else:
        form=AccountAuthenticationForm()
    context['login_form']=form

    return render(request,'account/login.html',context)


def account_view(request):
    if not request.user.is_authenticated:
        return redirect('account:login')

    context={}

    if request.POST:
        form=AccountUpdateForm(request.POST,instance=request.user)
        if form.is_valid():
            form.initial={
                'email':request.POST['email'],
                'username':request.POST['username']
            }
            form.save()
            context['success_message']='Account Updated Successfully!'
    else:
        form=AccountUpdateForm(
            initial={
                'email':request.user.email,
                'username':request.user.username,
            }
        )
    context['account_form']=form
    saved_hotels=Hotel.objects.filter(saved_by__email=request.user)
    savedHotels=list(map(Hotel.serialize,saved_hotels))
    for (index, hotel) in enumerate(savedHotels, start=1):
        hotel['id'] = index
        hotel['is_saved']=True
    context['savedHotels']=json.dumps(savedHotels)
    return render(request,'account/account.html',context)

def must_authenticate_view(request):
    return render(request,'account/must_authenticate.html')
