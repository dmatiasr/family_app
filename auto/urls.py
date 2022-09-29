from rest_framework import routers
from django.urls import include, path

from . import views


router = routers.DefaultRouter()
router.register("vehicles", viewset=views.VehicleViewSet, basename="vehicles")
router.register("services", viewset=views.ServiceViewSet, basename="services")


urlpatterns = [
    path("", include(router.urls)),
]
