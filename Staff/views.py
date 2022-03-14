from django.shortcuts import render
import datetime
from Order.models import Order


# Create your views here.
def StaffAppointments(request):
    year = request.GET.get("year", "None")
    month = request.GET.get("month")
    day = request.GET.get("day")
    today = datetime.datetime.now()

    if year and month and day:
        today = str(month) + " " + str(day) + "," + str(year)
        month = datetime.datetime.strptime(month, '%B').month
        order = Order.objects.filter(specialist=request.user,appointment_start_time__year=year, appointment_start_time__month=month,
                                     appointment_start_time__day=day)
    else:
        today = today.date()
        order = Order.objects.filter(specialist=request.user, appointment_start_time__gte=today)
    context = {
        "today":today,
        "order":order
    }
    return render(request,"home/appointments.html",context=context)