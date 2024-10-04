from django_filters import rest_framework as filters
from .models import Cat


class CatFilter(filters.FilterSet):
    color = filters.CharFilter(field_name='color', lookup_expr='icontains')
    age = filters.NumberFilter(field_name='age')
    breed = filters.CharFilter(field_name='breed__name', lookup_expr='icontains')

    class Meta:
        model = Cat
        fields = ('color', 'age', 'breed')
