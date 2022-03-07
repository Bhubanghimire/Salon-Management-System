from django.shortcuts import render
from Services.models import Service
from Accounts.models import About
from Common.models import ConfigChoice



# Create your views here.
def Home(request):
    service = ConfigChoice.objects.filter(category__name="Service")
    print(service)
    about = About.objects.all().first()

    context = {
        "about":about,
        "service":service
    }
    return render(request,"home/home.html", context=context)

def ServiceView(request):
    final_list=[]
    service = ConfigChoice.objects.filter(category__name="Service")
    for ser in service:
        service = Service.objects.filter(category=ser)
        json={
            "name":ser.name,
            "category":service
        }
        final_list.append(json)
    print(final_list)
    context = {
        "service": final_list
    }
    return render(request, "home/services.html", context=context)
