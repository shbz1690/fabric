"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserInformation(models.Model):
    firstName = models.CharField(max_length=128)
    lastName = models.CharField(max_length=128)
    institution = models.CharField(max_length=128)
    institutionNumber = models.CharField(max_length=128)
    cstaPI = models.CharField(max_length=128)
    orchidNumber = models.CharField(max_length=128)
    userId = models.OneToOneField(User)
