from django.db.models import Count
from rest_framework import generics
from django_filters import rest_framework as filters

from .filters import CatFilter
from .models import Cat, Breed
from .serializers import CatSerializer, BreedSerializer
from .permissions import IsOwnerOrReadOnly


class СatListApiView(generics.ListAPIView):
    queryset = Cat.objects.all().select_related('user', 'breed')
    serializer_class = CatSerializer


class CatRetrieveApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Cat.objects.all().select_related('user', 'breed')
    serializer_class = CatSerializer
    lookup_field = 'id'


class CatFilterApiView(generics.ListAPIView):
    queryset = Cat.objects.all().select_related('user', 'breed')
    serializer_class = CatSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CatFilter


class BreedListApiView(generics.ListAPIView):
    queryset = Breed.objects.all().annotate(count=Count('cats'))
    serializer_class = BreedSerializer
