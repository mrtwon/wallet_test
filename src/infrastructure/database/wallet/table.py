from sqlalchemy import Table, Column, UUID, NUMERIC, FLOAT

from src.infrastructure.database.base import mapper_registry
from src.infrastructure.database.wallet.model import WalletModel

wallet_table = Table(
    "wallet",
    mapper_registry.metadata,
    Column("wallet_id", UUID, primary_key=True, unique=True, nullable=False),
    Column("wallet_balance", FLOAT, nullable=False, default=0)
)

mapper_registry.map_imperatively(
    WalletModel,
    wallet_table
)