from ninja import Router

from .categories.route import router as category_router
from .products.route import router as product_router

v1_router = Router()

v1_router.add_router("v1", category_router)
v1_router.add_router("v1", product_router)
