from django.shortcuts import render,redirect
from .models import Order
from Common.models import ConfigChoice
from django.contrib.auth.decorators import login_required
from Services.models import Service, User
from datetime import datetime, timedelta


# Create your views here.
@login_required(login_url="login")
def CreateAppointment(request):
    categorys = ConfigChoice.objects.filter(category__name="Service", is_active=True)
    services = Service.objects.filter(is_deleted=False)
    user = User.objects.filter(user_type__name="Staff User")
    context = {
        "service": services,
        "users": user,
        "category": categorys
    }
    if request.method == 'POST':
        status = ConfigChoice.objects.get(name="Pending")
        service = request.POST.get('service')
        service = Service.objects.get(id=service)
        year = request.POST.get('year')
        month = request.POST.get('month')
        month = datetime.strptime(month, '%B').month

        date = request.POST.get('date')
        time = request.POST.get("time")
        date=str(year)+'-'+str(month)+"-"+str(date)+"T"+str(time)+":00"
        start_date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
        end_date = start_date+timedelta(hours=service.duration)

        order=Order.objects.filter(service=service)
        check=order.filter(appointment_start_time__lte=start_date,appointment_end_time__lte=end_date)

        if check:
            context["error"] = "Sorry Service is not available at this time."
            return render(request, 'home/newappointments.html',context=context)
        Order.objects.create(user=request.user, status=status, service=service, specialist=request.user,
                             appointment_start_time=start_date, appointment_end_time=end_date)
        return redirect('superadmin-appointments')

    else:
        return render(request, 'home/newappointments.html', context=context)