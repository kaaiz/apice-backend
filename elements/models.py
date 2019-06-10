from django.db import models
from django.utils import timezone
from PIL import Image

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Element(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    display = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

