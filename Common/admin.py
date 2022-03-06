from django.contrib import admin
from .models import ConfigChoice, ConfigCategory

# Register your models here.
@admin.register(ConfigCategory)
class Category(admin.ModelAdmin):
    list_display = ["id","name","description"]


@admin.register(ConfigChoice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ["id","name","description"]
    filter_display = ["is_active"]