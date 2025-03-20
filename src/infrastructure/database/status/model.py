from uuid import UUID

from src.infrastructure.database.base import entity


@entity
class StatusModel:
    status_id: str
