from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from Common.models import ConfigChoice

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
    email = models.EmailField(max_length=255, unique=True, verbose_name="Email Address")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=CHOICES)
    profile = models.ImageField(upload_to="profile", null=True)
    address = models.CharField(max_length=250)
    dob = models.DateField()
    phone = models.CharField(max_length=200)
    is_admin = models.BooleanField(default=False)
    position = models.CharField(max_length=250,default=" ")
    is_staff = models.BooleanField(default=False)
    user_type = models.ForeignKey(ConfigChoice, on_delete=models.CASCADE,null=True)
    description = models.TextField(default="")

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

User = get_user_model()


class Otp(models.Model):
    email = models.EmailField()
    otp = models.CharField(max_length=255)

    def __str__(self):
        return str(self.email)

    class Meta:
        verbose_name_plural = "OTP"


class ContactUs(models.Model):
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=250)
    message = models.TextField()

class About(models.Model):
    logo = models.ImageField(upload_to="about")
    cover = models.ImageField(upload_to="about")
    description = models.TextField()
    phone_1 = models.CharField(max_length=20)
    phone_2 = models.CharField(max_length=20)