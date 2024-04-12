from django.db import models

# Create your models here.
class Member(models.Model):
    memberId = models.AutoField(primary_key = True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)