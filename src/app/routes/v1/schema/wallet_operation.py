from datetime import datetime
from typing import Optional
from uuid import UUID

from src.app.routes.v1.schema.base import BaseSchema


class WalletOperationSchema(BaseSchema):
    wallet_operation_id: UUID
    operation_id: str
    status_id: str
    wallet_id: UUID
    amount: float
    create_at: datetime
    update_at: Optional[datetime] = None