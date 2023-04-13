from .models import Coverage, Plan
from rest_framework import viewsets, permissions
from .serializers import CoverageSerializer, PlanSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework_gis.filters import InBBoxFilter

# ViewSets define the view behavior Users.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# ViewSets define the view behavior Coverages.
class CoverageViewset(viewsets.ModelViewSet):
    queryset = Coverage.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CoverageSerializer

# ViewSets define the view behavior Plans.
class PlanViewset(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PlanSerializer

# ViewSets define the view behavior Location.
class LocationViewset(viewsets.ModelViewSet):
    queryset = Coverage.objects.all()
    serializer_class = CoverageSerializer
    bbox_filter_field = 'location'
    filter_backends = (InBBoxFilter,)
    bbox_filter_include_overlapping = True # Optional


