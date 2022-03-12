from django.db import models
from Common.models import ConfigChoice
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(ConfigChoice, on_delete=models.CASCADE)
    description = models.TextField()
    icon = models.ImageField(upload_to="service")
    price = models.DecimalField(max_digits=10, decimal_places=3)
    specialist = models.ForeignKey(User, on_delete=models.CASCADE)
    duration = models.IntegerField()
    is_deleted = models.BooleanField(default=False)


class Gallery(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to="gallery")
    service = models.ForeignKey(Service, on_delete=models.CASCADE)


class Testimonials(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
