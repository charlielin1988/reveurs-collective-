from django.contrib import admin
from .models import User, Location, Exhibition, Review

admin.site.register(User)
admin.site.register(Location)
admin.site.register(Exhibition)
admin.site.register(Review)

# Register your models here.
