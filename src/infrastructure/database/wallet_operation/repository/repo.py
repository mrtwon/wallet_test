from uuid import UUID

from sqlalchemy import select

from src.app.exception.exception import PropertyNotFoundException
from src.infrastructure.database._repo import SQLAlchemyRepo
from src.infrastructure.database.wallet_operation.model import WalletOperationModel
from src.infrastructure.database.wallet_operation.repository.interface import IWalletOperationRepo


class WalletOperationRepo(IWalletOperationRepo, SQLAlchemyRepo):
    async def add(self, model: WalletOperationModel) -> WalletOperationModel:
        self.session.add(model)
        return model

    async def update(self, model: WalletOperationModel) -> WalletOperationModel:
        await self.session.merge(model)
        await self.session.flush()
        return model

    async def get(self, wallet_id: UUID | None = None,
                  wallet_operation_id: UUID | None = None) -> WalletOperationModel | None:
        if wallet_id:
            stmt = select(WalletOperationModel).where(WalletOperationModel.wallet_id == wallet_id)
        elif wallet_operation_id:
            stmt = select(WalletOperationModel).where(WalletOperationModel.wallet_operation_id == wallet_operation_id)
        else:
            raise PropertyNotFoundException()
        return await self.session.scalar(stmt)

    async def get_all(self, wallet_id: UUID) -> list[WalletOperationModel]:
        stmt = select(WalletOperationModel).where(WalletOperationModel.wallet_id == wallet_id)
        result = await self.session.scalars(stmt)
        return result.all()