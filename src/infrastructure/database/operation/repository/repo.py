from sqlalchemy import select

from src.infrastructure.database._repo import SQLAlchemyRepo
from src.infrastructure.database.operation.model import OperationModel
from src.infrastructure.database.operation.repository.interface import IOperationRepo


class OperationRepo(IOperationRepo, SQLAlchemyRepo):
    async def get_all(self) -> list[OperationModel]:
        stmt = select(OperationModel)
        result = await self.session.scalars(stmt)
        return result.all()