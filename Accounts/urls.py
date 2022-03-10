from django.urls import path, include
from .views import SignupView,LoginView,Logout,Contact, AboutDetail,ProfileView,ProfileUpdateView,UserAppointments

urlpatterns = [
    path('signup/',SignupView, name='signup'),
    path('login/', LoginView, name="login"),
    path('logout/',Logout, name="logout"),
    path("contactus/",Contact,name="contactus"),
    path("about/",AboutDetail,name="about"),
    path("profile/id/details/",ProfileView,name="main-profile"),
    path("profile/id/edit/",ProfileUpdateView,name="profile-update"),
    path("all-appointments/", UserAppointments, name="user-appointments"),

]