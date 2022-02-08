from django.shortcuts import render
from .models import Location, Exhibition, Review


def location_list(request):
    locations = Location.objects.all()
    return render(request, 'reveurs/location_list.html', {'locations': locations})


def exhibition_list(request):
    exhibitions = Exhibition.objects.all()
    return render(request, 'reveurs/exhibition_list.html', {'exhibitions': exhibitions})


def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'reveurs/review_list.html', {'reviews': reviews})


# Create your views here.
