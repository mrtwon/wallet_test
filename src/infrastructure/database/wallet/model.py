import decimal
import uuid
from uuid import UUID

from attrs import field

from src.infrastructure.database.base import entity


@entity
class WalletModel:
    wallet_id: UUID = field(factory=uuid.uuid4)
    wallet_balance: decimal = field(default=0.0)
