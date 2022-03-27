from django.urls import path, include, re_path
# from django.conf.urls import re_path
from .views import SignupView,LoginView,Logout,Contact, AboutDetail,ProfileView,ProfileUpdateView,UserAppointments,DeleteUser,ContactList,ContactDelete, activate

urlpatterns = [
    path('signup/',SignupView, name='signup'),
    path('activate/<uidb64>/<token>/',activate, name='activate'),

    path('login/', LoginView, name="login"),
    path('logout/',Logout, name="logout"),
    path("contactus/",Contact,name="contactus"),
    path("about/",AboutDetail,name="about"),
    path("profile/<int:id>/details/",ProfileView,name="main-profile"),
    path("profile/<int:id>/edit/",ProfileUpdateView,name="profile-update"),
    path("all-appointments/", UserAppointments, name="user-appointments"),
    path("user/<int:id>/delete/", DeleteUser,name="user-delete"),
    path("contact/", ContactList,name="contactus-list"),
    path("contact/<int:id>/delete/", ContactDelete,name="contactus-delete"),

]