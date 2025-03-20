from typing import Protocol

from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.database.base import IUoW
from src.infrastructure.database.operation.repository.interface import IOperationRepo
from src.infrastructure.database.operation.repository.uow import IOperationUOW
from src.infrastructure.database.status.repository.interface import IStatusRepo
from src.infrastructure.database.status.repository.uow import IStatusUOW
from src.infrastructure.database.wallet.repository.interface import IWalletRepo
from src.infrastructure.database.wallet.repository.uow import IWalletUOW
from src.infrastructure.database.wallet_operation.repository.interface import IWalletOperationRepo
from src.infrastructure.database.wallet_operation.repository.uow import IWalletOperationUOW


class SQLAlchemyBaseUOW(IUoW):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def commit(self) -> None:
        await self._session.commit()

    async def rollback(self) -> None:
        await self._session.rollback()


class SQLAlchemyUoW(
    SQLAlchemyBaseUOW,
    IWalletUOW,
    IWalletOperationUOW,
    IOperationUOW,
    IStatusUOW
):
    wallet: type[IWalletRepo]
    wallet_operation: type[IWalletOperationRepo]
    operation: type[IOperationRepo]
    status: type[IStatusRepo]

    def __init__(
            self,
            session: AsyncSession,
            wallet: type[IWalletRepo],
            wallet_operation: type[IWalletOperationRepo],
            operation: type[IOperationRepo],
            status: type[IStatusRepo]
    ):
        self.wallet = wallet(session)
        self.wallet_operation = wallet_operation(session)
        self.status = status(session)
        self.operation = operation(session)
        super().__init__(session)
