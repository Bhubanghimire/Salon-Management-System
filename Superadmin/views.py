from django.shortcuts import render, redirect
from Common.models import ConfigChoice,ConfigCategory
from Services.models import Service
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
User = get_user_model()

@login_required(login_url="login")
def SettingView(request):
    category = ConfigChoice.objects.filter(category__name="Service",is_active=True)
    service = Service.objects.filter(is_deleted=False)
    user = User.objects.filter(user_type__name="Staff User")
    print(user)

    context = {
        "service":service,
        "user":user,
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
            ConfigChoice.objects.create(name=category,image=image,description=description, category=ConfigCategory.objects.get(name="Service"),is_active=True)
        except Exception as e:
            error = "Category Already exists."
        context = {
            "error":error,
            "user":user,
            "service": service,
            "category":categorys
        }
        return render(request, "home/setting.html",context=context)

def DeleteService(request,id):
    service = Service.objects.get(id=id)
    service.is_deleted = True
    service.save()
    return redirect("profile")


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
    return redirect("profile")

def AddService(request):
    categorys = ConfigChoice.objects.filter(category__name="Service", is_active=True)
    service = Service.objects.filter(is_deleted=False)
    user = User.objects.filter(user_type__name="Staff User")
    print(user)


    if request.method == 'POST' and request.FILES['image']:
        service_name = request.POST.get("servicename")
        description = request.POST.get("servicedescription")
        price = request.POST.get("serviceprice")
        category = request.POST.get("category")
        user = request.POST.get("user")
        cover = request.FILES["image"]
        try:
            Service.objects.create(specialist=User.objects.get(id=user),name=service_name,description=description,price=price,category=ConfigChoice.objects.get(id=category),icon=cover)
        except Exception:
            context = {
                "service": service,
                "user": user,
                "service_error":"Service Name Already Exists!",
                "category": categorys
            }
            return render(request, "home/setting.html", context=context)

        return redirect("profile")
    return redirect("profile")
