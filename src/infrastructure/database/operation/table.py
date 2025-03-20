from sqlalchemy import Table, Column, String, UUID

from src.infrastructure.database.base import mapper_registry
from src.infrastructure.database.operation.model import OperationModel

operation_table = Table(
    "operation",
    mapper_registry.metadata,
    Column("operation_id", String, primary_key=True, unique=True, nullable=False)
)

mapper_registry.map_imperatively(
    OperationModel,
    operation_table
)