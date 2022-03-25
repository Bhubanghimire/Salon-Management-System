import datetime
from Order.models import Order
from django.shortcuts import render, redirect
from Common.models import ConfigChoice,ConfigCategory
from Services.models import Service, Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
User = get_user_model()

@login_required(login_url="login")
def SettingView(request):
    category = ConfigChoice.objects.filter(category__name="Service")
    service = Service.objects.filter(is_deleted=False)
    user = User.objects.filter(user_type__name="Staff User")
    # print(u.user_type__name)

    context = {
        "service":service,
        "users":user,
        "category":category
    }
    return render(request, "home/setting.html", context=context)

def AddCategory(request):
    categorys = ConfigChoice.objects.filter(category__name="Service", is_active=True)
    user = User.objects.filter(user_type__name="Staff User")
    service = Service.objects.filter(is_deleted=False)
    if request.method == 'POST' and request.FILES['image']:
        error = None
        category = request.POST.get("category")
        image = request.FILES["image"]
        print(image)
        description = request.POST.get("description")
        print(description)
        try:
            ConfigChoice.objects.create(name=category,image=image,deSuperadminAppointmentsscription=description, category=ConfigCategory.objects.get(name="Service"),is_active=True)
        except Exception as e:
            error = "Category Already exists."
        context = {
            "error":error,
            "users":user,
            "service": service,
            "category":categorys
        }
        return render(request, "home/setting.html",context=context)

def DeleteService(request,id):
    service = Service.objects.get(id=id)
    service.is_deleted = True
    service.save()
    return redirect("admin-dashboard")


def EditService(request,id):
    service = Service.objects.get(id=id)
    if request.method == 'POST':
        service_name = request.POST.get("servicename")
        description = request.POST.get("servicedescription")
        price = request.POST.get("serviceprice")
        category = request.POST.get("category")
        print(category)
        service.name = service_name
        service.description = description
        service.price =price
        service.category = ConfigChoice.objects.get(id=category)
    service.save()
    return redirect("admin-dashboard")

def AddService(request):
    categorys = ConfigChoice.objects.filter(category__name="Service", is_active=True)
    service = Service.objects.filter(is_deleted=False)
    user = User.objects.filter(user_type__name="Staff User")

    if request.method == 'POST' and request.FILES['image']:
        service_name = request.POST.get("servicename")
        description = request.POST.get("servicedescription")
        price = request.POST.get("serviceprice")
        duration = request.POST.get("serviceduration")
        category = request.POST.get("category")
        user = request.POST.get("user")
        cover = request.FILES["image"]
        try:
            Service.objects.create(name=service_name,duration=int(duration),description=description,price=price,category=ConfigChoice.objects.get(id=category),icon=cover)
        except Exception as e:
            context = {
                "service": service,
                "users": user,
                "service_error":str(e),   #"Service Name Already Exists!",
                "category": categorys
            }
            return render(request, "home/setting.html", context=context)

        return redirect("admin-dashboard")
    return redirect("admin-dashboard")


def SuperadminAppointments(request):
    year = request.GET.get("year","None")
    month = request.GET.get("month")
    day = request.GET.get("day")
    today = datetime.datetime.now()

    if year and month and day:
        today = str(month) + " " + str(day)+","+str(year)
        month = datetime.datetime.strptime(month, '%B').month

        order = Order.objects.filter(appointment_start_time__year=year,appointment_start_time__month=month,appointment_start_time__day=day)
    else:
        today = today.date()
        order = Order.objects.filter(appointment_start_time__gte=today)


    status = ConfigChoice.objects.filter(category__name="Status")
    user = User.objects.filter(user_type__name="Staff User")

    context = {
        "status": status,
        "users": user,
        "today":today,
        "order":order
    }
    return render(request,"home/appointments.html",context=context)

def UserList(request):
    print("bhuban")
    user = User.objects.filter(user_type__name="Normal User")
    context = {
        "users": user
    }
    return render(request,'home/userlist.html',context=context)


def StaffList(request):
    user = User.objects.filter(user_type__name="Staff User", is_delete=False)
    print(user)
    context = {
        "users": user
    }
    return render(request,'home/stafflist.html',context=context)

def Inventory(request):
    product = Product.objects.all()
    type = ConfigChoice.objects.filter(category__name="Product")
    return render(request, 'home/inventory.html',{"products":product,"type":type})