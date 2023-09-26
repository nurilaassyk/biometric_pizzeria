from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name='Created date', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Updated date', auto_now_add=True)

    class Meta:
        abstract = True
