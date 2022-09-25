from rest_framework import routers

from django.urls import include, path

from . import views


router = routers.DefaultRouter()
router.register("auto", viewset=views.VehicleViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
