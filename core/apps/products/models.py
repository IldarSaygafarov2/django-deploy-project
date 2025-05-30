from django.db import models
from django.urls import reverse

from core.apps.common.models import BaseModel


def show_product_image_path(instance, filename: str) -> str:
    return f"products/{instance.pk}/previews/{filename}"


class Product(BaseModel):
    name = models.CharField(verbose_name="Название", max_length=150, unique=True)
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    quantity = models.PositiveIntegerField(default=5, verbose_name="Кол-во")
    image = models.ImageField(
        verbose_name="Заставка",
        upload_to=show_product_image_path,
        null=True,
        blank=True,
    )
    price = models.FloatField(verbose_name="Цена")
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.CASCADE,
        related_name="categories",
        verbose_name="Категория",
    )

    def __str__(self) -> str:
        return self.name

    def get_image(self):
        if not self.image:
            return 'https://stilsoft.ru/images/catalog/noup.png'
        return self.image.url

    def get_absolute_url(self):
        return reverse('product_detail_page', kwargs={'product_id': self.pk})

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


def show_product_image_upload_path(instance, filename: str) -> str:
    return f"products/{instance.product.pk}/gallery/{filename}"


class ProductImage(BaseModel):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="Продукт",
    )
    image = models.ImageField(
        verbose_name="Фото",
        upload_to=show_product_image_upload_path,
    )

    class Meta:
        verbose_name = "Фото продукта"
        verbose_name_plural = "Фото продукта"
