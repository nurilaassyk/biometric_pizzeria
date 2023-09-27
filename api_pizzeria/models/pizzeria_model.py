from django.db import models

from api_pizzeria.models.base_model import BaseModel


class PizzeriaModel(BaseModel):
    name = models.CharField(verbose_name='Name', blank=True, null=True)
    address = models.CharField(verbose_name='Address', blank=True, null=True)
