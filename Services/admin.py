from django.contrib import admin
from .models import Service


# Register your models here.
@admin.register(Service)
class OTPAdmin(admin.ModelAdmin):
    list_display = ["id"]