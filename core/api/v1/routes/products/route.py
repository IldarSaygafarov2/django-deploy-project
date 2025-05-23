from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from ninja import Router

from core.api.core.schemas.product.dto import ProductSchema
from core.apps.products.models import Product

router = Router(tags=["Products"])


@router.get("/products/", response=list[ProductSchema])
def get_all_products(request: HttpRequest):
    products = Product.objects.all()
    return products


@router.get('/products/{product_id}', response=ProductSchema)
def get_product(request: HttpRequest, product_id: int):
    product = get_object_or_404(Product, id=product_id)
    return product
