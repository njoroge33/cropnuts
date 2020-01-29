from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
import datetime

YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))
# Create your models here.

class Crate(models.Model):
    country =CountryField(default = 'Kenya')
    year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    
    def __str__(self):
       return self.country
