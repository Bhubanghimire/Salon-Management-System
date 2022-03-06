from django.db import models


# Create your models here.
class ConfigCategory(models.Model):
    type = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return str(self.type)

    class Meta:
        verbose_name_plural ="CONFIG CATEGORY"


class ConfigChoice(models.Model):
    value = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    image=models.ImageField(upload_to="choice/", blank=True)
    category = models.ForeignKey(ConfigCategory, on_delete=models.CASCADE, verbose_name="choice")

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name_plural ="CONFIG CHOICE"