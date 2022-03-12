from django.urls import path, include
from .views import CreateAppointment,CancelAppointment,UpdateAppointment


urlpatterns = [
    path("new/",CreateAppointment, name="create-new"),
    path("appointment/<uuid:uuid>/cancel/", CancelAppointment, name="cancel-appointment"),
    path('appointment/<uuid:uuid>/update/',UpdateAppointment, name="appointment-update"),

    ]