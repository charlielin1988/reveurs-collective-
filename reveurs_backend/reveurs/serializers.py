from rest_framework import serializers
from .models import Location, Exhibition, Review


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    exhibitions = serializers.HyperlinkedRelatedField(
        view_name='exhibition_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Location
        fields = ('id', 'user', 'city', 'start_date', 'end_date',)


class ExhibitionSerializer(serializers.HyperlinkedModelSerializer):
    location = serializers.HyperlinkedRelatedField(
        view_name='location_detail',
        read_only=True
    )

    class Meta:
        model = Exhibition
        fields = ('id', 'location', 'title',
                  'description', 'picture', 'location_id')


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    location = serializers.HyperlinkedRelatedField(
        view_name='location_detail',
        read_only=True
    )

    class Meta:
        model = Review
    fields = ('id', 'location', 'location_id', 'title', 'content')
