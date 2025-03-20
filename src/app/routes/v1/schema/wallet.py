from uuid import UUID

from src.app.routes.v1.schema.base import BaseSchema


class WalletSchema(BaseSchema):
    wallet_id: UUID
    wallet_balance: float


class WalletOperation(BaseSchema):
    operation_type: str
    amount: float
