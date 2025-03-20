from uuid import UUID

from src.app.routes.v1.schema.base import BaseSchema


class OperationSchema(BaseSchema):
    operation_id: str