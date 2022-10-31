import django.contrib.auth.models
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from .managers import UserManager
from products.models import Product


class User(AbstractUser):
    email = models.EmailField(verbose_name='email', unique=True)
    username = ...
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    mobile = PhoneNumberField(null=False, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    favourite_products = models.ManyToManyField(Product, default=None, blank=True)

    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name

    @property
    def get_favourite_products(self):
        favourite_products = Product.objects.prefetch_related().filter(user=self.id)
        return favourite_products
