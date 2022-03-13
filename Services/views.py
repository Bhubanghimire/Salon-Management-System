from django.shortcuts import render, redirect
from Services.models import Service,Gallery,Testimonials, Product
from Accounts.models import About
from Common.models import ConfigChoice, ConfigCategory


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


def AddproductType(request):
    if request.method=="POST":
        type = request.POST.get("type")
        try:
            category = ConfigCategory.objects.get(name="Product")
        except Exception:
            category = ConfigCategory.objects.get(name="Product", description="Product")
        try:
            ConfigChoice.objects.create(name=type, category=category,description=type, is_active=True)
            return redirect("inventory")
        except Exception:
            product = Product.objects.all()
            type = ConfigChoice.objects.filter(category__name="Product")
            return render(request, 'home/inventory.html', {"products": product, "type": type,"type_error":"This Product Type already exists."})


def AddProduct(request):
    if request.method=="POST":
        name=request.POST.get("name")
        type=request.POST.get("type")
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")
        Product.objects.create(name=name,type=ConfigChoice.objects.get(id=type),price=price,quantity=quantity)
        return redirect("inventory")


def EditProduct(request,id):
    product = Product.objects.filter(id=id)
    if request.method=="POST":
        name=request.POST.get("name")
        type=request.POST.get("type")
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")
        product.update(name=name,type=type,price=price,quantity=quantity)
        return redirect("inventory")


def DeleteProduct(request,id):
    Product.objects.filter(id=id).delete()
    return redirect("inventory")