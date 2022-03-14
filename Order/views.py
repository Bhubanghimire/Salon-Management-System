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
        specialist = User.objects.filter(service=service,on_leave=False)
        check=order.filter(appointment_start_time__lte=start_date,appointment_end_time__gte=end_date,specialist__in=specialist)

        if check:
            context["error"] = "Sorry Service is not available at this time."
            return render(request, 'home/newappointments.html',context=context)
        Order.objects.create(user=request.user, status=status, service=service, specialist=specialist.first(),
                             appointment_start_time=start_date, appointment_end_time=end_date,payment_complete=False)
        return redirect('superadmin-appointments')

    else:
        return render(request, 'home/newappointments.html', context=context)


@login_required(login_url="login")
def CancelAppointment(request, uuid):
    ord =Order.objects.filter(uuid=uuid).first()
    ord.status=ConfigChoice.objects.get(name="Cancelled")
    ord.save()
    if request.user.user_type.name=="Super User":
        return redirect("superadmin-appointments")
    elif request.user.user_type.name=="Staff User":
        return redirect("staff-appointments")
    else:
        return redirect("user-appointments")


def UpdateAppointment(request, uuid):
    if request.method == 'POST':
        appointment = Order.objects.get(uuid=uuid)
        staff = request.POST.get('staff')
        user = User.objects.get(id=staff)
        status = request.POST.get('status')

        year = request.POST.get('year')
        month = request.POST.get('month')
        if not month.isdigit():
            month = datetime.strptime(month, '%B').month
        start_time = request.POST.get('start_time')
        end_time= request.POST.get('start_time')
        date = request.POST.get("date")


        appointment.specialist = user
        appointment.status = ConfigChoice.objects.get(id=status)
        appointment.appointment_start_time =str(year)+'-'+str(month)+"-"+str(date)+"T"+str(start_time)+":00"
        appointment.appointment_end_time =str(year)+'-'+str(month)+"-"+str(date)+"T"+str(end_time)+":00"

        appointment.save()
        if request.user.user_type.name == "Super User":
            return redirect("superadmin-appointments")
        elif request.user.user_type.name == "Staff User":
            return redirect("staff-appointments")
        else:
            return redirect("user-appointments")

from django.db.models import Sum


@login_required(login_url="login")
def Makepayment(request):
    today = datetime.today()
    orders = Order.objects.filter(appointment_start_time__gte=today,user=request.user, payment_complete=False)
    total = orders.aggregate(Sum('service__price'))["service__price__sum"]
    context = {
        "orders":orders,
        "total":total,
        "today":today
    }
    return render(request, "home/payment.html", context=context)