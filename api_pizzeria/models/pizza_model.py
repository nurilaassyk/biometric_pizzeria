from django.db import models

from api_pizzeria.models.base_model import BaseModel


class PizzaModel(BaseModel):
    name = models.CharField(verbose_name='Name', blank=True, null=True)
    cheese = models.CharField(verbose_name='Types of cheese', blank=True, null=True)
    dough = models.CharField(verbose_name='Dough thickness', blank=True, null=True)
    secret_ingredient = models.CharField(verbose_name='Secret ingredient', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='Created date', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Updated date', auto_now_add=True)
    deleted_at = models.BooleanField(verbose_name='Deleted at', default=False)
