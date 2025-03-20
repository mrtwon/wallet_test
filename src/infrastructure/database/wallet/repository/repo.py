from uuid import UUID

from sqlalchemy import select

from src.infrastructure.database._repo import SQLAlchemyRepo
from src.infrastructure.database.wallet.model import WalletModel
from src.infrastructure.database.wallet.repository.interface import IWalletRepo


class WalletRepo(IWalletRepo, SQLAlchemyRepo):
    async def add(self, model: WalletModel) -> WalletModel:
        print('input')
        self.session.add(model)
        print('output')
        return model

    async def update(self, model: WalletModel) -> WalletModel:
        await self.session.merge(model)
        await self.session.flush()
        return model

    async def get(self, wallet_id: UUID) -> WalletModel:
        stmt = select(WalletModel).where(WalletModel.wallet_id == wallet_id)
        result = await self.session.scalar(stmt)
        return result
