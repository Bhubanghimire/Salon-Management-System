from django.shortcuts import render, redirect
from Services.models import Service,Gallery,Testimonials
from Accounts.models import About
from Common.models import ConfigChoice


# Create your views here.
def Home(request):
    service = ConfigChoice.objects.filter(category__name="Service")
    gallery = Gallery.objects.all()
    about = About.objects.all().first()

    context = {
        "gallery":gallery,
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


def ReviewView(request):
    review = Testimonials.objects.all()
    if request.method == 'POST':
        message = request.POST.get("message")
        user = request.user
        try:
            Testimonials.objects.create(user=user,message=message)
            return redirect('home')
        except Exception:
            error = "Please login to send review."
            return render(request, 'home/review.html', {"review": review,"error":error})
    return render(request,'home/review.html',{"review":review})