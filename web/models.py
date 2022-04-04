import email
from django.db import models

from django.conf import settings

settings.configure()

import django
django.setup()

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    number = models.IntegerField()
    zip = models.IntegerField()