from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Coverage, Plan
from django.contrib.auth.models import User

# Serializers define the API representation to Users.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_staff']

# Serializers define the API representation to Coverages.
class CoverageSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Coverage
        geo_field = "location"
        auto_bbox = True

        fields = ('id', 'color', 'address', 'plans')

# Serializers define the API representation to Plans.
class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('id', 'name')

