from random import choices
from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Properties(models.Model):
    address = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rent = models.IntegerField(null=True)
    propType = models.CharField(max_length=10)
    occupied = models.BooleanField(default=False)

    def __str__(self):
        return self.address

class Renter(models.Model):
    name = models.CharField(max_length = 30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.OneToOneField(Properties, on_delete = models.CASCADE)
    homeAddr = models.TextField()
    phNo = models.CharField(max_length=10)
    email = models.EmailField()
    dateJoined = models.DateField()
    dateLeft = models.DateField(null = True, blank = True)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    renter = models.ForeignKey(Renter, on_delete = models.CASCADE)
    paid = models.IntegerField(null=True,blank=True)
    dues = models.IntegerField(null=True,blank=True)
    balance = models.IntegerField(default = 0)
    date = models.DateField()

    def __str__(self):
        return self.renter.name

