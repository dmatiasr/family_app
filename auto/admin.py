from django.contrib import admin
from auto.models import (
    Automovil, 
    Service,
)


class AutomovilAdmin(admin.ModelAdmin):
    pass


class ServiceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Automovil, AutomovilAdmin)
admin.site.register(Service, ServiceAdmin)
