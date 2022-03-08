from django.urls import path, include
from .views import SettingView,AddCategory,DeleteService, EditService,AddService

urlpatterns = [
    path("setting/", SettingView,name="setting"),
    path("add-category/", AddCategory, name="add-category"),
    path("service/<int:id>/delete/",DeleteService, name="delete-service"),
    path("service/<int:id>/edit/",EditService, name="edit-service"),
    path("add-service/",AddService,name='add-service'),
    ]