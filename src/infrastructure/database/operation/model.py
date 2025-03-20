from uuid import UUID

from src.infrastructure.database.base import entity


@entity
class OperationModel:
    operation_id: str
