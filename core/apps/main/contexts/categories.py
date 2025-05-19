from django.http import HttpRequest

from core.apps.categories.models import Category


def get_all_categories(request: HttpRequest) -> dict[str, list[Category]]:
    return {"categories": Category.objects.all()}
