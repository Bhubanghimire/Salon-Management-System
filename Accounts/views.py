from Common.models import ConfigChoice
from Order.models import Order
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
from datetime import datetime
from django.contrib.auth import login as auth_login
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import ContactUs
from Services.models import Service
from django.contrib.auth import get_user_model
User = get_user_model()
import datetime


def SignupView(request):
    user_type = ConfigChoice.objects.filter(category__name="User Type").exclude(name="Super User")
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


        if month.isnumeric():
            month = int(month)

        elif isinstance(month, str):
            month = datetime.datetime.strptime(month, '%B').month
        else:
            error = "Enter valid Month."
            return render(request, 'home/signup.html', {"error": error, "user_type": user_type})
        password2 = request.POST.get("confirm_password")
        dob = datetime.datetime(year=int(year), month=month, day=int(day))


        test= User.objects.filter(email=email).first()
        if test:
            error = "User Already Exists."

            return render(request, 'home/signup.html', {"error": error, "user_type":user_type})

        if password1 == password2:
            user = User.objects.create_user(email=email,profile="Static/images/user-placeholder.jpg",password=password1, first_name=first_name,last_name=last_name, user_type=ConfigChoice.objects.get(id=int(role)),address=address,phone=phone,dob=dob,gender=gender)
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


def ProfileView(request, id):
    user = User.objects.get(id=id)
    return render(request, 'home/profile.html', {"user_obj":user})


def ProfileUpdateView(request, id):
    user_obj = User.objects.filter(id=id)
    user= user_obj.first()
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    email = request.POST.get("email")
    phone = request.POST.get("phone")
    address = request.POST.get("address")
    gender = request.POST.get("gender")
    salary = request.POST.get("salary")
    leave =request.POST.get("leave",None)
    service = request.POST.get("service",None)
    year = request.POST.get("year")
    month = request.POST.get("month")
    day = request.POST.get("day")
    date=str(year)+"-"+str(month)+"-"+str(day)

    try:
        if request.method=="POST" and request.FILES['image']:
            image = request.FILES["image"]
            user.profile.delete()
            user.profile = image
            user.save()
            user_obj.update(email=email,dob=date, first_name=first_name, last_name=last_name, phone=phone, address=address,gender=gender)
            if salary:
                user_obj.update(salary=salary)
            if leave:
                user_obj.update(on_leave=True)
            else:
                user_obj.update(on_leave=False)
            
            if service:
                user_obj.update(service = Service.objects.get(id=service))
            
            return redirect("main-profile", id=id)

    except Exception as e:
        user_obj.update(email=email, dob=date,first_name=first_name, last_name=last_name, phone=phone, address=address,gender=gender)
        if salary:
            user_obj.update(salary=salary)
        if leave:
            user_obj.update(on_leave=True)
        else:
            user_obj.update(on_leave=False)

        if service:
            user_obj.update(service = Service.objects.get(id=service))

        
        return redirect("main-profile",id=id)
    else:
        if user.service:
            service = Service.objects.filter(is_deleted=False).exclude(id=user.service.id)
        return render(request, 'home/update_profile.html', {"user_obj":user,"service":service})


def UserAppointments(request):

    year = request.GET.get("year", "None")
    month = request.GET.get("month")
    day = request.GET.get("day")
    today = datetime.datetime.now()

    if year and month and day:
        today = str(month) + " " + str(day) + "," + str(year)
        month = datetime.datetime.strptime(month, '%B').month
        order = Order.objects.filter(user=request.user, appointment_start_time__year=year,
                                     appointment_start_time__month=month,
                                     appointment_start_time__day=day)
        context = {
            "today": today,
            "order": order
        }
    else:
        today =today.date()
        order = Order.objects.filter(user=request.user,appointment_start_time__date=today)

        context = {
            "today": today,
            "order": order
            }
    return render(request, "home/appointments.html", context=context)



def DeleteUser(request,id):
    User.objects.filter(id=id).update(is_delete=True)
    return redirect("staff-list")


def ContactList(request):
    contact = ContactUs.objects.all()
    return render(request, "home/allcontactus.html", {"contactus":contact})

def ContactDelete(request,id):
    ContactUs.objects.filter(id=id).delete()
    return redirect("contactus")