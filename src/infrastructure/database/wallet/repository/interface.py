from typing import Protocol
from uuid import UUID

from src.infrastructure.database.wallet.model import WalletModel


class IWalletRepo(Protocol):
    async def add(self, model: WalletModel) -> WalletModel:
        ...

    async def update(self, model: WalletModel) -> WalletModel:
        ...

    async def get(self, wallet_id: UUID) -> WalletModel:
        ...
