from  django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
# from .forms import *
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
from django.http import HttpResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import ContactUs
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


def Contact(request):
    print("start")
    if request.method == 'POST':
        print("come")
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print(message)

        try:
            ContactUs.objects.create(full_name=full_name,email=email,phone=phone,message=message)

            return redirect('home')
        except Exception as e:
            return render(request, 'home/contactus.html',{"error":str(e)})
    else:
        print("error")
        return render(request, 'home/contactus.html')

