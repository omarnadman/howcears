import email
from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    number = models.IntegerField()
    zip = models.IntegerField(max_length=6)