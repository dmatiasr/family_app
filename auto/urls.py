from rest_framework import routers
from django.urls import include, path

from . import views


router = routers.DefaultRouter()
router.register("vehicles", viewset=views.VehicleViewSet, basename="vehicles")


urlpatterns = [
    path("", include(router.urls)),
]
