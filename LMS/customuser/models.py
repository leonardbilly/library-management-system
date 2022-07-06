from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=500)
    date_of_birth = models.DateField(null=True)
    phone_number = models.BigIntegerField()
    sex = models.CharField(max_length=10, null=True)
    role = models.CharField(max_length=20, default='Student')

    REQUIRED_FIELDS = ['name', 'email', 'sex', 'role', 'phone_number']

    def __str__(self):
        return self.name


class UserPayment(models.Model):
    book_id = models.BigIntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=50, default='Pending')
    amount = models.CharField(max_length=50, default='O UGX')

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.description[0:20]
