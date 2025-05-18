from django import template
from core.apps.categories.models import Category


register = template.Library()


@register.simple_tag()
def get_all_categories() -> list[Category]:
    return list(Category.objects.all())
