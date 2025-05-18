from django.http import HttpRequest
from ninja import Router
from core.api.core.schemas.product.dto import ProductSchema
from core.apps.products.models import Product


router = Router(tags=["Products"])


@router.get("/products/", response=list[ProductSchema])
def get_all_products(request: HttpRequest):
    products = Product.objects.all()
    return products
