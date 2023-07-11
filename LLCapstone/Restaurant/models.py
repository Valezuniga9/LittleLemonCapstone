from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=225)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'


class Booking(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    bookingDate = models.DateTimeField()

    def __str__(self):
        return self.name

