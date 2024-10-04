from rest_framework import serializers
from .models import *


class BreedSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Breed
        fields = '__all__'


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ('rate', 'comment')

    def validate_rate(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rate must be between 1 and 5.")
        return value


class CatSerializer(serializers.ModelSerializer):
    comments = RateSerializer(many=True, read_only=True)
    average_rating = serializers.FloatField(read_only=True)
    breed = BreedSerializer(read_only=True)

    class Meta:
        model = Cat
        fields = '__all__'
