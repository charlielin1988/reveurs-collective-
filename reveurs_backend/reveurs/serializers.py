from rest_framework import serializers
from .models import Location


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    exhibitions = serializers.HyperlinkedRelatedField(
        view_name='exhibition_detail',
        many=True,
        read_only=True
    )
