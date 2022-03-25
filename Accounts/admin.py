from django.contrib import admin
from .models import MyUser, Otp,ContactUs, About

# Register your models here.
# Register your models here.
@admin.register(MyUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", 'first_name','last_name',"email",'user_type',"is_delete"]
    list_filter = ["user_type"]

@admin.register(Otp)
class OTPAdmin(admin.ModelAdmin):
    list_display = ["id","email","otp"]


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ["id"]


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ["id","logo","description"]