from django.db import models


class User(models.Model):
    fullname = models.CharField(max_length=30)
    birthday = models.DateField()
    email = models.EmailField()
    about = models.CharField(max_length=100)
