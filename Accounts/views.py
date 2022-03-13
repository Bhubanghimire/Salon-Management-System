from Common.models import ConfigChoice
from Order.models import Order
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
from datetime import datetime
from django.contrib.auth import login as auth_login
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import ContactUs
from django.contrib.auth import get_user_model
User = get_user_model()
import datetime


def SignupView(request):
    user_type = ConfigChoice.objects.filter(category__name="User Type")
    if request.method == 'POST':
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        year = request.POST.get("year")
        month = request.POST.get("month")
        day = request.POST.get("date")
        password1 = request.POST.get("password")
        role = request.POST.get("role")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        gender = request.POST.get("gender")
        month = datetime.strptime(month, '%B').month
        password2 = request.POST.get("confirm_password")
        dob = datetime(year=int(year), month=month, day=int(day))

        print(gender)
        print(role)
        print("data received")
        test= User.objects.filter(email=email).first()
        if test:
            error = "User Already Exists."

            return render(request, 'home/signup.html', {"error": error, "user_type":user_type})

        if password1 == password2:
            user = User.objects.create_user(email=email,password=password1, first_name=first_name,last_name=last_name, user_type=ConfigChoice.objects.get(id=int(role)),address=address,phone=phone,dob=dob,gender=gender)
            auth_login(request, user)
            return redirect('home')
        else:
            error = "Please enter same password."
            return render(request, 'home/signup.html', {"error":error,"user_type":user_type})
    else:
        return render(request, 'home/signup.html',{"user_type":user_type})


def LoginView(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request,email=email, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            Result="Email password doesnt matched"
            return render(request, 'home/signin.html', {'results': Result})
    else:
        return render(request, 'home/signin.html')




def Logout(request):
    logout(request)
    return redirect('home')


def Contact(request):
    print("start")
    if request.method == 'POST':
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        try:
            ContactUs.objects.create(full_name=full_name,email=email,phone=phone,message=message)
            return redirect('home')
        except Exception as e:
            return render(request, 'home/contactus.html',{"error":str(e)})
    else:
        return render(request, 'home/contactus.html')

def AboutDetail(request):
    staff = User.objects.filter(Q(user_type__name="Staff User") | Q(user_type__name="Super User"))
    return render(request, 'home/about.html',{"staff":staff})

def ProfileView(request):
    return render(request, 'home/profile.html')

def ProfileUpdateView(request):
    return render(request, 'home/update_profile.html')

def UserAppointments(request):
    today = datetime.datetime.now()
    order = Order.objects.filter(user=request.user,appointment_start_time__date=today)
    context = {
        "today": today.date(),
        "order": order
    }
    return render(request, "home/appointments.html", context=context)

def Makepayment(request):
    return render(request, "home/payment.html")
