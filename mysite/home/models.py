from django.db import models
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.urls import path
from django.conf import settings

class Land(models.Model):
    title = models.CharField(max_length=100)
    size = models.PositiveIntegerField()  # Size in square meters
    location = models.CharField(max_length=100)
    land_type = models.CharField(max_length=50, choices=[
        ('residential', 'Жилая'),
        ('agricultural', 'Сельскохозяйственная'),
        ('commercial', 'Коммерческая'),
    ])
    image = models.ImageField(upload_to='lands/')

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    land = models.ForeignKey('Land', on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending')

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"
