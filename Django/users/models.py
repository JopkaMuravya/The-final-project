from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default_avatar.png')
    level = models.IntegerField(default=1)
    rank = models.CharField(max_length=50, default='Новичок')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=500.00)

    def __str__(self):
        return self.username