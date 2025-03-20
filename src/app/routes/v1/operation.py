from fastapi import APIRouter, Depends

from src.app.di.setup import BaseUOW
from src.app.routes.v1.schema.operation import OperationSchema
from src.infrastructure.database.uow import SQLAlchemyUoW

operation_router = APIRouter(prefix='/operation')


@operation_router.get('/', response_model=list[OperationSchema])
async def get_operation_router(
        repo: BaseUOW = Depends()
):
    result = await repo.operation.get_all()
    return [OperationSchema.model_validate(one) for one in result]
