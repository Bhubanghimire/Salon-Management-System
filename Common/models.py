from django.db import models


# Create your models here.
class ConfigCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural ="CONFIG CATEGORY"


class ConfigChoice(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    image=models.ImageField(upload_to="choice/", blank=True)
    is_active = models.BooleanField()
    category = models.ForeignKey(ConfigCategory, on_delete=models.CASCADE, verbose_name="choice")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural ="CONFIG CHOICE"