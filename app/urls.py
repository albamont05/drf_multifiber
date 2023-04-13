from django.urls import path, include
from rest_framework import routers
from .api import CoverageViewset, PlanViewset, UserViewSet, LocationViewset

router = routers.DefaultRouter()

router.register('api/users', UserViewSet, 'users')
router.register('api/plans', PlanViewset, 'plans')
router.register('api/coverages', CoverageViewset, 'coverages')
router.register('api/location', LocationViewset, 'locations')

urlpatterns = [
    path('', include(router.urls)),
]




