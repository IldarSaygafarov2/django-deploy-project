from ninja import NinjaAPI
from .v1 import api_router

api = NinjaAPI(
    title="Test api for deployed project",
    description="This is test api",
)

api.add_router("", api_router)
