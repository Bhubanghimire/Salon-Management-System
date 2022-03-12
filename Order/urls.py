from django.urls import path, include
from .views import CreateAppointment


urlpatterns = [
    path("new/",CreateAppointment, name="create-new"),

    ]