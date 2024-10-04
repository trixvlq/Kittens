from django.db.models import Count, Avg
from rest_framework import generics
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated

from .filters import CatFilter
from .models import Cat, Breed, Rate
from .serializers import CatSerializer, BreedSerializer, RateSerializer
from .permissions import IsOwnerOrReadOnly, IsNotAuthor


class СatListApiView(generics.ListAPIView):
    queryset = Cat.objects.all().select_related('user', 'breed').annotate(
        average_rating=Avg('comments__rate')
    )
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


class CatCreateApiView(generics.CreateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = [IsAuthenticated]


class CatRateApiView(generics.CreateAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    permission_classes = [IsNotAuthor]

    def perform_create(self, serializer):
        user = self.request.user

        cat_id = self.kwargs.get('id')
        cat = Cat.objects.get(id=cat_id)

        serializer.save(user=user, cat=cat)


class BreedListApiView(generics.ListAPIView):
    queryset = Breed.objects.all().annotate(count=Count('cats'))
    serializer_class = BreedSerializer
