from django.urls import path, include
from .views import SignupView,LoginView,Logout,Contact

urlpatterns = [
    path('signup/',SignupView, name='signup'),
    path('login/', LoginView, name="login"),
    path('logout/',Logout, name="logout"),
    path("contactus/",Contact,name="contactus"),
    ]