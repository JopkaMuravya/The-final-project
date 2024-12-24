from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default_avatar.png')
    level = models.IntegerField(default=1)
    rank = models.CharField(max_length=50, default='Новичок')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=500.00)

    def __str__(self):
        return self.username


class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks')
    executor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks_taken')
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=50)
    reward = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    tags = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title