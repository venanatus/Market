from django.shortcuts import render, redirect
from .forms import *
from .urls import *
from django.contrib.auth import login, logout


def sign_up(request):
    form = SignUpForm(request.POST)
    form2 = TypeChoise(request.POST)
    if form.is_valid() and request.method == 'POST':
        user = form.save()
        user.save()
        if form2.is_valid():
            a = request.POST.get('a')
            if a == 'admin':
                login(request, user)
                return redirect('shop:create')
            if a == 'user':
                login(request, user)
                return redirect('auth:create_profile')
    form = SignUpForm()
    return render(request, 'register.html', {'form': form, 'form2': form2})


def create_profile(request):
    form = ProfileForm(request.POST or None, request.FILES)
    if request.method == 'POST' and form.is_valid():
        a = form.save(commit=False)
        a.user = request.user
        a.save()
        return redirect('shop:home')
    return render(request, 'create_profile.html', {'form': form})


# def sign_up(request):
#     form = SignUpForm(request.POST)
#     if request.method == 'POST':
#         if form.is_valid():
#             user = form.save()
#             return redirect('auth:a')
#     return render(request, 'register.html', {'form': form})


def a(request):
    form = LoginForm(data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('shop:home')
    return render(request, 'login.html', {'form': form})


def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile.html', {'profile': profile})


def out(request):
    logout(request)
    return redirect('shop:home')
