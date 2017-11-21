# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# We have created an extension(one to one relationship) of inbuilt user models provided by django
class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return 'Username: ' + str(self.user)
