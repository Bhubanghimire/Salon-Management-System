from django.contrib import admin
from .models import Order,Invoice

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["uuid","user","specialist"]

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ["id",]