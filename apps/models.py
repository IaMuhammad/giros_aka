import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    class Roles(models.TextChoices):
        COOK = 'cook', 'Cook'
        WAITER = 'waiter', 'Waiter'

    role = models.CharField(max_length=255, choices=Roles.choices, default=Roles.WAITER)


class Meal(models.Model):
    class Type(models.TextChoices):
        DRINK = 'drink', 'Ichimlik'
        MEAL = 'meal', 'Ovqat'
        SALAT = 'salat', 'Salat'

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=Type.choices, default=Type.MEAL)
    image = models.ImageField(upload_to='meals/')

    def __str__(self):
        return str(self.name)


class Table(models.Model):
    number = models.IntegerField(null=True)
    image = models.ImageField(upload_to='cafe')

    def __str__(self):
        return str(self.number)


class Order(models.Model):
    table = models.ForeignKey('apps.Table', on_delete=models.CASCADE)
    meals = models.ManyToManyField('apps.Meal', through='apps.OrderMeal')


class OrderMeal(models.Model):
    order = models.ForeignKey('apps.Order', on_delete=models.CASCADE)
    meal = models.ForeignKey('apps.Meal', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
