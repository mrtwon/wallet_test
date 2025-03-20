
from sqlalchemy import Table, Column, String, UUID

from src.infrastructure.database.base import mapper_registry
from src.infrastructure.database.status.model import StatusModel

status_table = Table(
    "status",
    mapper_registry.metadata,
    Column("status_id", String, primary_key=True, unique=True)
)

mapper_registry.map_imperatively(
    StatusModel,
    status_table
)