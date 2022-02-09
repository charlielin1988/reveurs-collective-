from rest_framework import serializers
from .models import Location, Exhibition, Review


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    exhibitions = serializers.HyperlinkedRelatedField(
        view_name='exhibition_detail',
        many=True,
        read_only=True
    )
    location_url = serializers.ModelSerializer.serializer_url_field(
        view_name='location_detail')

    class Meta:
        model = Location
        fields = ('id', 'location_url', 'city', 'start_date',
                  'end_date', 'exhibitions')


class ExhibitionSerializer(serializers.HyperlinkedModelSerializer):
    location = serializers.HyperlinkedRelatedField(
        view_name='location_detail',
        read_only=True)

    location_id = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(),
        source='location')

    class Meta:
        model = Exhibition
        fields = ('id', 'location', 'location_id',
                  'title', 'picture', 'description', )


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    location = serializers.HyperlinkedRelatedField(
        view_name='location_detail',
        read_only=True)

    location_id = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(),
        source='location')

    class Meta:
        model = Review
        fields = ('id', 'location', 'location_id',
                  'title', 'content', 'username')
