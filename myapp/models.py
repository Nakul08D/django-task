from django.db import models
from django.contrib.auth.models import User


class book(models.Model):
    name=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    pages=models.IntegerField()
    price=models.IntegerField()
    
    def __str__(self):
        return self.name
