from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
import uuid


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an Email address")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password=password, **extra_fields)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        (' ',' ')
    )
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True, verbose_name="Email Address")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=CHOICES)
    description = models.CharField(max_length=255, default="")
    phone = models.CharField(max_length=20, default="")
    dob = models.DateField(null=True, blank=True)
    profile_img = models.ImageField(upload_to="profile", null=True, blank=True)
    verified_user = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


    class Meta:
        verbose_name_plural = "USER"

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)


class Otp(models.Model):
    email = models.EmailField()
    otp = models.CharField(max_length=255)

    def __str__(self):
        return str(self.email)

    class Meta:
        verbose_name_plural = "OTP"


User = get_user_model()