from django.shortcuts import render,redirect
from .models import Order
from Common.models import ConfigChoice
from django.contrib.auth.decorators import login_required
from Services.models import Service, User
from datetime import datetime, timedelta
from django.contrib import messages


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

        order=Order.objects.filter(service=service).exclude(status__name="Cancelled")
        specialist = User.objects.filter(service=service.id,on_leave=False)


        if len(specialist)==0:
            context["error"] = "Sorry Specialist is not available at this time."
            return render(request, 'home/newappointments.html', context=context)

        test_case1 = order.filter(appointment_start_time__lte=start_date,appointment_end_time__gte=end_date,specialist__in=specialist)
        test_case2 = order.filter(specialist__in=specialist, appointment_start_time__range=[start_date, end_date])
        test_case3 = order.filter(specialist__in=specialist, appointment_end_time__range=[start_date, end_date])
        check = test_case1 | test_case2 | test_case3

        if len(check)>0:
            special_list=[]
            for i in check:
                special_list.append(i.specialist.id)

            specialist= specialist.exclude(id__in=specialist)
            if len(specialist)==0:
                context["error"] = "Sorry Service is not available at this time."
                return render(request, 'home/newappointments.html',context=context)

        Order.objects.create(user=request.user, status=status, service=service, specialist=specialist.first(),
                             appointment_start_time=start_date, appointment_end_time=end_date,payment_complete=False)
        if request.user.user_type.name == "Super User":
            return redirect("superadmin-appointments")
        elif request.user.user_type.name == "Staff User":
            return redirect("staff-appointments")
        else:
            return redirect("user-appointments")

    else:
        return render(request, 'home/newappointments.html', context=context)

from datetime import datetime, timezone
@login_required(login_url="login")
def CancelAppointment(request, uuid):
    ord =Order.objects.filter(uuid=uuid).first()

    if request.user.user_type.name=="Super User":
        ord.status = ConfigChoice.objects.get(name="Cancelled")
        ord.save()
        return redirect("superadmin-appointments")

    elif request.user.user_type.name=="Staff User":
        now = datetime.now(timezone.utc)
        order_time = ord.order_time
        diff = now-order_time
        hrs = diff.days * 24 + diff.seconds / 3600.0

        if hrs<24:
            ord.status = ConfigChoice.objects.get(name="Cancelled")
            ord.save()
        return redirect("staff-appointments")

    else:
        return redirect("user-appointments")


def UpdateAppointment(request, uuid):
    if request.method == 'POST':
        appointment = Order.objects.get(uuid=uuid)
        service = appointment.service
        staff = request.POST.get('staff')
        user = User.objects.get(id=staff)
        status = request.POST.get('status')
        year = request.POST.get('year')
        month = request.POST.get('month')
        if not month.isdigit():
            month = datetime.strptime(month, '%B').month
        start_time = request.POST.get('start_time_data')
        end_time= request.POST.get('end_time_data')
        date = request.POST.get("date")

        specialist = user
        appointment.status = ConfigChoice.objects.get(id=status)
        start_date = str(year) + '-' + str(month) + "-" + str(date) + "T" + str(start_time) + ":00"
        end_date = str(year)+'-'+str(month)+"-"+str(date)+"T"+str(end_time)+":00"

        test1= datetime.strptime(start_date,'%Y-%m-%dT%H:%M:%S')
        test2= datetime.strptime(end_date, '%Y-%m-%dT%H:%M:%S')
        if test1>test2:
            messages.error(request, 'Sorry Invalid time.')
            if request.user.user_type.name == "Super User":
                return redirect("superadmin-appointments")
            elif request.user.user_type.name == "Staff User":
                return redirect("staff-appointments")
            else:
                return redirect("user-appointments")


        order = Order.objects.filter(service=service).exclude(status__name="Cancelled")
        order = order.exclude(uuid=uuid)

        test_case1 = order.filter(appointment_start_time__lte=start_date, appointment_end_time__gte=end_date,specialist=specialist)
        test_case2 = order.filter(specialist=specialist, appointment_start_time__range=[start_date, end_date])
        test_case3 = order.filter(specialist=specialist, appointment_end_time__range=[start_date, end_date])

        check = test_case1 | test_case2 | test_case3
        if len(check) > 0:
            messages.error(request, 'Can not update sorry.')
            if request.user.user_type.name == "Super User":
                return redirect("superadmin-appointments")
            elif request.user.user_type.name == "Staff User":
                return redirect("staff-appointments")
            else:
                return redirect("user-appointments")

        appointment.specialist = specialist
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
    orders1 = Order.objects.filter(appointment_start_time__gte=today,user=request.user, payment_complete=False)
    total = orders1.aggregate(Sum('service__price'))["service__price__sum"]

    context = {
        "orders":orders1,
        "total":total,
        "today":today
    }
    return render(request, "home/payment.html", context=context)


@login_required(login_url="login")
def PaymentComplete(request):
    today = datetime.today()
    orders = Order.objects.filter(appointment_start_time__gte=today, user=request.user, payment_complete=False)
    orders.update(payment_complete=True)
    return redirect("make-payment")

