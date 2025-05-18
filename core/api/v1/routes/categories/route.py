from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from ninja import Router

from core.api.core.schemas.category.dto import CategorySchema, CategoryCreateSchema
from core.apps.categories.models import Category

router = Router(tags=["Categories"])


@router.get("/categories/", response=list[CategorySchema])
def get_all_categories(request: HttpRequest):
    categories = Category.objects.all()
    return categories


@router.get('/categories/{pk}', response=CategorySchema)
def get_category_detail(request: HttpRequest, pk: int):
    category = get_object_or_404(Category, pk=pk)
    return category


@router.post("/categories/", response=CategorySchema)
def create_category(request: HttpRequest, category_data: CategoryCreateSchema):
    category = Category.objects.create(**category_data.dict())
    return category
