from django.db import models

# Create your models here.


class Location(models.Model):
    city = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    location_picture = models.TextField(default='null')

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


class Review(models.Model):
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE,
        related_name='reviews'
    )
    username = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
