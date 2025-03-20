from typing import Protocol
from uuid import UUID

from src.infrastructure.database.wallet_operation.model import WalletOperationModel


class IWalletOperationRepo(Protocol):
    async def add(self, model: WalletOperationModel) -> WalletOperationModel:
        ...

    async def update(self, model: WalletOperationModel) -> WalletOperationModel:
        ...

    async def get(self, wallet_id: UUID | None = None,
                  wallet_operation_id: UUID | None = None) -> WalletOperationModel | None:
        ...

    async def get_all(self, wallet_id: UUID) -> list[WalletOperationModel]:
        ...