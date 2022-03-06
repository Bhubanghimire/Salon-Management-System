from  django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
# from .forms import *
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
from django.http import HttpResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
# from allauth.account.views import LoginView, SignupView

def Inactive(request):
    return HttpResponse("<h1>You are inactive.<br>Please contact administration.</h1>")

def SignupView(request):
    if request.method == 'POST':
        pass
    #     form = SignUpForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         auth_login(request, user)
    #         return redirect('home')
    # else:
    #     form = SignUpForm()
    return render(request, 'home/signup.html')


def LoginView(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
        print(password)
        user = authenticate(request,email=email, password=password)
        print(user)
        if user:
            login(request, user)
            return redirect('home')
        else:
            Result="Email password doesnt matched"
            return render(request, 'home/signin.html', {'results': Result})
    else:
        return render(request, 'home/signin.html')
    # return render(request, 'account/login.html', {'form': form})




def Logout(request):
    logout(request)
    return redirect('home')