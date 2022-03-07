from django.urls import path, include
from .views import Home, ServiceView

urlpatterns = [
    path("",Home,name="home"),
    path("service", ServiceView,name="service"),
    ]