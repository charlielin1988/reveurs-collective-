from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    pronouns = models.CharField(max_length=100)
    profile_pic = models.TextField()
    email = models.CharField(max_length=100)
    passwordDigest = models.CharField(max_length=100)


def __str__(self):
    return self.name
