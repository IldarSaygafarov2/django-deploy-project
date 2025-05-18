from ninja import Schema
from datetime import datetime


class CategorySchema(Schema):
    id: int
    name: str
    created_at: datetime
    updated_at: datetime


class CategoryCreateSchema(Schema):
    name: str
