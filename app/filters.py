from rest_framework_gis.filterset import GeoFilterSet
from rest_framework_gis.filters import GeometryFilter
from django_filters import filters

from .models import Coverage

class LocationFilter(GeoFilterSet):
    slug = filters.CharFilter(name='slug', lookup_expr='istartswith')
    contains_geom = GeometryFilter(name='locacion', lookup_expr='contains')
    
    filter_overrides = {}

    class Meta:
        model = Coverage