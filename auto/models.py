from django.db import models


class Automovil(models.Model):
    name = models.CharField(max_length=50)
    matricula = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return self.name


class Service(models.Model):
    applied_date = models.DateField()
    name = models.CharField(default="", max_length=50)
    description = models.TextField()
    technician = models.CharField(default="", max_length=50)
    price = models.CharField(max_length=50)
    related_vehicle = models.ForeignKey(
        Automovil, null=True, blank=True, default="None", on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name
