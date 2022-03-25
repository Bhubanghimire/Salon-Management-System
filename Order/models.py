import uuid
from django.db import models
from Common.models import ConfigChoice
from Services.models import Service
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
User = get_user_model()


# Create your models here.
class Order(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.ForeignKey(ConfigChoice, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    specialist = models.ForeignKey(User, on_delete=models.CASCADE,related_name="specialist")
    order_time = models.DateTimeField(auto_now_add=True)
    appointment_start_time = models.DateTimeField()
    appointment_end_time = models.DateTimeField()
    payment_complete = models.BooleanField()

    def __str__(self):
        return str(self.user)

