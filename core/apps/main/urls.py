from django.urls import path
from . import views


urlpatterns = [
    path("", views.show_home_page, name="home_page"),
    path('categories/<int:category_id>/', views.show_category_products_page, name='category_products_page'),
    path('products/<int:product_id>/', views.show_product_detail_page, name='product_detail_page')
]
