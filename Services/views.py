from django.shortcuts import render
from Services.models import *
from Accounts.models import About

# Create your views here.
def Home(request):
    about = About.objects.all().first()
    context = {
        "about":about
    }
    return render(request,"home/home.html", context=context)