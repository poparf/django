from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)


class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    age = models.IntegerField(max_length=2)
    university = models.CharField(max_length=50)
    university_year = models.integerField(max_length=1)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    iq = models.IntegerField(max_length=3)