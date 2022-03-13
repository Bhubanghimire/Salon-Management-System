from django.urls import path, include
from .views import SettingView,AddCategory,DeleteService, EditService,AddService,SuperadminAppointments,UserList,StaffList,Inventory

urlpatterns = [
    path("configuration/", SettingView,name="admin-dashboard"),
    path("add-category/", AddCategory, name="add-category"),
    path("service/<int:id>/delete/",DeleteService, name="delete-service"),
    path("service/<int:id>/edit/",EditService, name="edit-service"),
    path("add-service/",AddService,name='add-service'),
    path("all-appointments/", SuperadminAppointments,name="superadmin-appointments"),
    path("user-lists/", UserList,name="user-list"),
    path("staff-lists/", StaffList,name="staff-list"),
    path("inventory/", Inventory,name="inventory"),
    ]