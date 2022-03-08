from django.contrib import admin
from .models import Service, Gallery, Testimonials


# Register your models here.
@admin.register(Service)
class OTPAdmin(admin.ModelAdmin):
    list_display = ["id","name","category","description"]


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ["id"]


@admin.register(Testimonials)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["id","user","message"]