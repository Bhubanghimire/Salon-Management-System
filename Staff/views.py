from django.shortcuts import render
import datetime
from Order.models import Order


# Create your views here.
def StaffAppointments(request):
    today = datetime.datetime.now()
    order = Order.objects.filter(specialist=request.user, appointment_start_time__gte=today)
    context = {
        "today":today.date(),
        "order":order
    }
    return render(request,"home/appointments.html",context=context)