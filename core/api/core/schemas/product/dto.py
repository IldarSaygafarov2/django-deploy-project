from typing import Optional

from ninja import Schema
from core.api.core.schemas.category.dto import CategorySchema


class ProductImageSchema(Schema):
    id: int
    image: str


class ProductSchema(Schema):
    id: int
    name: str
    description: Optional[str]
    image: Optional[str]
    price: float
    category: CategorySchema
    images: Optional[list[ProductImageSchema]]
