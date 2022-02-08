from rest_framework import generics
from .serializers import LocationSerializer, ExhibitionSerializer, ReviewSerializer
from .models import Location, Exhibition, Review


class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class ExhibitionList(generics.ListCreateAPIView):
    queryset = Exhibition.objects.all()
    serializer_class = ExhibitionSerializer


class ExhibitionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exhibition.objects.all()
    serializer_class = ExhibitionSerializer


class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


# Create your views here.
