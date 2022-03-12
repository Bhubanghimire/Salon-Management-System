from django.urls import path, include
from .views import *

urlpatterns = [
    path("all-appointments/", StaffAppointments, name="staff-appointments"),

]