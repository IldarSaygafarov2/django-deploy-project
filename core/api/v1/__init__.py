from ninja import Router
from .routes import v1_router


api_router = Router()

api_router.add_router("api/", v1_router)
