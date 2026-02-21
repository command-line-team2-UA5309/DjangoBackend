from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('regular', 'Regular'),
        ('silver', 'Silver'),
        ('golden', 'Golden'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='regular')
    is_banned = models.BooleanField(default=False)
