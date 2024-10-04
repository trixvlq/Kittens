from django.db.models import Count
from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *


class СatListApiView(generics.ListAPIView):
    queryset = Cat.objects.all().select_related('user', 'breed')
    serializer_class = CatSerializer


class BreedListApiView(generics.ListAPIView):
    queryset = Breed.objects.all().annotate(count=Count('cats'))
    serializer_class = BreedSerializer
