

# models.py in your user app
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, role='customer', **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, role='admin', **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, username, password, role='admin', **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField()
    username = models.CharField(max_length=100, unique=True)
    dorm_number = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')], blank=False, null=True)
    full_name = models.CharField(max_length=200, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='user/photos/', null=True, blank=True)
    phone_number = models.CharField(max_length=20, blank=False, null=True)

    CUSTOMER = 'customer'
    RESTAURANT_OWNER = 'restaurant_owner'
    DELIVERY_PERSON = 'delivery_person'
    ADMIN = 'admin'
    
    USER_ROLES = [
        (CUSTOMER, 'Customer'),
        (RESTAURANT_OWNER, 'Restaurant Owner'),
        (DELIVERY_PERSON, 'Delivery Person'),
        (ADMIN, 'Admin'),
    ]

    role = models.CharField(max_length=20, choices=USER_ROLES, default=CUSTOMER)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'dorm_number', 'gender', 'full_name', 'profile_picture', 'phone_number']

    def __str__(self):
        return self.username

    @property
    def is_anonymous(self):
        return super().is_anonymous
