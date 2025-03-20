from fastapi import APIRouter, Depends

from src.app.di.setup import BaseUOW
from src.app.routes.v1.schema.status import StatusSchema
from src.infrastructure.database.status.repository.interface import IStatusRepo
from src.infrastructure.database.uow import SQLAlchemyUoW

router_status = APIRouter(prefix='/status')


@router_status.get('/', response_model=list[StatusSchema])
async def get_status_router(
        repo: BaseUOW = Depends()
):
    result = await repo.status.get_all()
    return [StatusSchema.model_validate(one) for one in result]
