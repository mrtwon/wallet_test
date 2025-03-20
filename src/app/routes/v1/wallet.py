import datetime
from uuid import UUID

from fastapi import APIRouter, Depends

from src.app.di.setup import BaseUOW
from src.app.exception.exception import WalletNotFound, NotEnoughMoneyException, UnknownMoneyOperationException
from src.app.routes.v1.schema.wallet import WalletSchema, WalletOperation
from src.app.routes.v1.schema.wallet_operation import WalletOperationSchema
from src.infrastructure.database.base import IUoW
from src.infrastructure.database.uow import SQLAlchemyUoW
from src.infrastructure.database.wallet.model import WalletModel
from src.infrastructure.database.wallet_operation.model import WalletOperationModel

wallet_router = APIRouter(prefix='/wallet')


@wallet_router.get('/{wallet_id}', response_model=WalletSchema)
async def get_wallet_router(
        wallet_id: UUID,
        repo: BaseUOW = Depends()
):
    result = await repo.wallet.get(wallet_id)
    if result is None:
        raise WalletNotFound()
    return result


@wallet_router.post('/', response_model=WalletSchema)
async def add_wallet_router(
    repo: BaseUOW = Depends()
):
    new_wallet_operation = WalletModel()
    result = await repo.wallet.add(new_wallet_operation)
    await repo.commit()
    return WalletSchema.model_validate(result)


@wallet_router.post('/{wallet_id}/operations', response_model=WalletOperationSchema)
async def operation_wallet_router(
        schema: WalletOperation,
        wallet_id: UUID,
        repo: BaseUOW = Depends(),
):
    result_get_wallet = await repo.wallet.get(wallet_id)
    if result_get_wallet is None:
        raise WalletNotFound()

    if schema.operation_type == 'DEPOSIT':
        new_wallet_operation_2 = WalletOperationModel(
            operation_id=schema.operation_type,
            status_id='CREATE',
            wallet_id=wallet_id,
            amount=schema.amount
        )
        print('DEPOSIT <><>')
        print(new_wallet_operation_2.wallet_operation_id)
        await repo.wallet_operation.add(new_wallet_operation_2)
        await repo.commit()
        try:
            result_get_wallet.wallet_balance = result_get_wallet.wallet_balance + schema.amount
            await repo.wallet.update(result_get_wallet)

            new_wallet_operation_2.status_id = 'CONFIRM'
            new_wallet_operation_2.update_at = datetime.datetime.now()
            await repo.wallet_operation.update(new_wallet_operation_2)
            await repo.commit()
        except Exception as e:
            print(e)
            new_wallet_operation_2.status_id = 'CANCEL'
            new_wallet_operation_2.update_at = datetime.datetime.now()
            await repo.wallet_operation.update(new_wallet_operation_2)
            await repo.commit()

    elif schema.operation_type == 'WITHDRAW':
        if 0.0 > (result_get_wallet.wallet_balance - schema.amount):
            raise NotEnoughMoneyException()
        new_wallet_operation_2 = WalletOperationModel(
            operation_id=schema.operation_type,
            status_id='CREATE',
            wallet_id=wallet_id,
            amount=schema.amount
        )
        print('WITHDRAW <><>')
        print(new_wallet_operation_2.wallet_operation_id)
        await repo.wallet_operation.add(new_wallet_operation_2)
        await repo.commit()
        try:
            result_get_wallet.wallet_balance = result_get_wallet.wallet_balance - schema.amount
            await repo.wallet.update(result_get_wallet)

            new_wallet_operation_2.status_id = 'CONFIRM'
            await repo.wallet_operation.update(new_wallet_operation_2)
            await repo.commit()
        except Exception:
            new_wallet_operation_2.status_id = 'CANCEL'
            await repo.wallet_operation.update(new_wallet_operation_2)
            await repo.commit()
    else:
        raise UnknownMoneyOperationException()
    return WalletOperationSchema.model_validate(new_wallet_operation_2)


@wallet_router.get('/{wallet_id}/operations', response_model=list[WalletOperationSchema])
async def all_operations_wallet_router(
        wallet_id: UUID,
        repo: BaseUOW = Depends()
):
    result_get_wallet = await repo.wallet_operation.get(wallet_id)
    if result_get_wallet is None:
        raise WalletNotFound()
    result = await repo.wallet_operation.get_all(wallet_id)
    return [WalletOperationSchema.model_validate(one) for one in result]