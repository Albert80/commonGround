import uuid
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.
class Product(models.Model):
  id = models.CharField(max_length=100, primary_key=True)
  name = models.CharField(max_length=55)
  value = models.DecimalField(max_digits=6, decimal_places=1)
  discount_value= models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
  stock = models.PositiveIntegerField(default=0)
  createdAt = models.DateTimeField(auto_now_add=True)
  updatedAt = models.DateTimeField(auto_now=True)

  def __str__(self):
      return self.name
