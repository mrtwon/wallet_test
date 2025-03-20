from typing import Protocol

from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from src.config import settings
from src.infrastructure.database.operation.repository.interface import IOperationRepo
from src.infrastructure.database.operation.repository.repo import OperationRepo
from src.infrastructure.database.operation.repository.uow import IOperationUOW
from src.infrastructure.database.status.repository.interface import IStatusRepo
from src.infrastructure.database.status.repository.repo import StatusRepo
from src.infrastructure.database.status.repository.uow import IStatusUOW
from src.infrastructure.database.uow import SQLAlchemyUoW, IUoW, SQLAlchemyBaseUOW
from src.infrastructure.database.wallet.repository.interface import IWalletRepo
from src.infrastructure.database.wallet.repository.repo import WalletRepo
from src.infrastructure.database.wallet.repository.uow import IWalletUOW
from src.infrastructure.database.wallet_operation.repository.interface import IWalletOperationRepo
from src.infrastructure.database.wallet_operation.repository.repo import WalletOperationRepo
from src.infrastructure.database.wallet_operation.repository.uow import IWalletOperationUOW


class Session(Protocol):
    pass


async def get_session() -> AsyncSession:
    async_engine = create_async_engine(
        url=settings.DATABASE_URL_asyncpg
    )

    session = async_sessionmaker(async_engine)
    async with session(expire_on_commit=False) as s:
        yield s


def get_uow(session: Session = Depends()):
    return SQLAlchemyUoW(
        session=session,
        wallet=WalletRepo,
        wallet_operation=WalletOperationRepo,
        operation=OperationRepo,
        status=StatusRepo
    )


# class BaseUOW:
#     wallet: IWalletRepo
#     wallet_operation: IWalletOperationRepo
#     operation: IOperationRepo
#     status: IStatusRepo

class BaseUOW(
    IWalletUOW,
    IWalletOperationUOW,
    IOperationUOW,
    IStatusUOW
):
    ...


def di_setup(app: FastAPI):
    app.dependency_overrides[Session] = get_session
    app.dependency_overrides[BaseUOW] = get_uow
