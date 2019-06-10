from django.db import models
from django.utils import timezone
from PIL import Image

class Category(models.Model):
    title = models.CharField(max_length=100, default="")
    text = models.TextField(null = True, default="", blank=True)
    image = models.ImageField(upload_to='images/', null = True, default="", blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Element(models.Model):
    title = models.CharField(max_length=100, default="")
    text = models.TextField(null = True, default="", blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null = True, default="", blank=True)
    display = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

