from sqlalchemy import Table, Column, UUID, ForeignKey, NUMERIC, TIMESTAMP, String, FLOAT

from src.infrastructure.database.base import mapper_registry
from src.infrastructure.database.wallet_operation.model import WalletOperationModel

wallet_operations = Table(
    "wallet_operation",
    mapper_registry.metadata,
    Column("wallet_operation_id", UUID, primary_key=True, unique=True, nullable=False),
    Column("operation_id", String, ForeignKey("operation.operation_id")),
    Column("status_id", String, ForeignKey("status.status_id")),
    Column("wallet_id", UUID, ForeignKey("wallet.wallet_id")),
    Column("amount", FLOAT, nullable=False),
    Column("create_at", TIMESTAMP, nullable=False),
    Column("update_at", TIMESTAMP, nullable=True)
)

mapper_registry.map_imperatively(
    WalletOperationModel,
    wallet_operations
)