from django.urls import path, include
from .views import SignupView,LoginView,Logout,Contact, AboutDetail,ProfileView,ProfileUpdateView,UserAppointments,DeleteUser

urlpatterns = [
    path('signup/',SignupView, name='signup'),
    path('login/', LoginView, name="login"),
    path('logout/',Logout, name="logout"),
    path("contactus/",Contact,name="contactus"),
    path("about/",AboutDetail,name="about"),
    path("profile/<int:id>/details/",ProfileView,name="main-profile"),
    path("profile/<int:id>/edit/",ProfileUpdateView,name="profile-update"),
    path("all-appointments/", UserAppointments, name="user-appointments"),
    path("user/<int:id>/delete/", DeleteUser,name="user-delete")

]