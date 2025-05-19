from django.http import HttpRequest

from django.shortcuts import render, get_object_or_404

from core.apps.categories.models import Category
from core.apps.products.models import Product


def show_home_page(request: HttpRequest):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, "main/index.html", context)


def show_category_products_page(request: HttpRequest, category_id: int):
    category = get_object_or_404(Category, pk=category_id)
    products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'products': products
    }
    return render(request, 'main/categories.html', context)


def show_product_detail_page(request: HttpRequest, product_id: int):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product
    }
    return render(request, 'main/product_detail.html', context)