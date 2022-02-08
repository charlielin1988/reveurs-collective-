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


class Location(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='locations')
    city = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()


def __str__(self):
    return self.city


class Exhibition(models.Model):
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name='exhibitions')
    title = models.CharField(max_length=100)
    description = models.TextField()
    picture = models.TextField()

    def __str__(self):
        return self.title
