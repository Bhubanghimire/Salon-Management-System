from django.db import models
from Common.models import ConfigChoice
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(ConfigChoice, on_delete=models.CASCADE)
    description = models.TextField()
    icon = models.ImageField(upload_to="service")
    price = models.DecimalField(max_digits=10, decimal_places=3)
    specialist = models.ForeignKey(User, on_delete=models.CASCADE)
