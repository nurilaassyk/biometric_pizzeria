from django.db import models

from api_pizzeria.models.base_model import BaseModel


class PizzaModel(BaseModel):
    pizzeria = models.ForeignKey(to='api_pizzeria.PizzeriaModel', verbose_name='Pizzeria', related_name='pizza',
                                 on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Name', blank=True, null=True)
    cheese = models.CharField(verbose_name='Types of cheese', blank=True, null=True)
    dough = models.CharField(verbose_name='Dough thickness', blank=True, null=True)
    secret_ingredient = models.CharField(verbose_name='Secret ingredient', blank=True, null=True)
