from rest_framework import serializers
from .models import *


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'


class CatSerializer(serializers.ModelSerializer):
    breed = BreedSerializer(read_only=True)

    class Meta:
        model = Cat
        fields = '__all__'


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'

    def validate_rate(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rate must be between 1 and 5.")
        return value
