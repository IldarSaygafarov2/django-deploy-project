from django.db import models
from django.urls import reverse

from core.apps.common.models import BaseModel


class Category(BaseModel):
    name = models.CharField(verbose_name="Название", unique=True)

    def __str__(self) -> str:
        return str(self.name)

    def get_absolute_url(self):
        return reverse('category_products_page', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
