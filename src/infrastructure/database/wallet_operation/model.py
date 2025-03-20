import datetime
import uuid
from typing import Optional
from uuid import UUID

from attrs import field
from pydantic import Field

from src.infrastructure.database.base import entity


@entity
class WalletOperationModel:
    wallet_operation_id: UUID = field(factory=uuid.uuid4)
    operation_id: str
    status_id: str
    wallet_id: UUID
    amount: float
    create_at: datetime.datetime = field(factory=datetime.datetime.now)
    update_at: Optional[datetime.datetime] = None
