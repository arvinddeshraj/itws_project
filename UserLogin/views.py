# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from .models import UserProfile
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from .forms import UserForm
from django.views import generic
from django.views.decorators.csrf import csrf_exempt


def indexView(request):
	logout(request)
	template_name='UserLogin/home.html'
	return render(request,template_name)

@csrf_exempt
def registerView(request):
    logout(request)
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            new_user_profile = UserProfile()
            new_user_profile.user = new_user
            new_user_profile.save()
            login(request,new_user)
            return HttpResponseRedirect('/sensors/')
    else:
        form=UserForm()

    return render(request,'UserLogin/registration_form.html',{'form':form})                        

@csrf_exempt
def loginView(request):
    logout(request)
    if request.method=='POST':
        form=UserForm(request.POST)
        try:
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(username=username,password=password)
            login(request,user)
            return HttpResponseRedirect('/sensors/')
        except Exception:
            return HttpResponseRedirect(reverse('UserLogin:login'))
    else:
        form = UserForm()
    return render(request,'UserLogin/login_form.html',{'form':form})
