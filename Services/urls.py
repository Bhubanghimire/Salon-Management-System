from django.urls import path, include
from .views import Home, ServiceView,ReviewView

urlpatterns = [
    path("",Home,name="home"),
    path("service", ServiceView,name="service"),
    path("review/",ReviewView,name="review"),
    ]