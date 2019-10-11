from django.db import models

class CustomerUser(models.Model):
    username = models.CharField(max_length=50, blank=True, default='',unique=True)
    password = models.CharField(max_length=50, blank=True, default='')