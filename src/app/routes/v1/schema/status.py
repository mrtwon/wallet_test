from uuid import UUID

from src.app.routes.v1.schema.base import BaseSchema


class StatusSchema(BaseSchema):
    status_id: str
