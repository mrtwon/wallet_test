from sqlalchemy import select

from src.infrastructure.database._repo import SQLAlchemyRepo
from src.infrastructure.database.status.model import StatusModel
from src.infrastructure.database.status.repository.interface import IStatusRepo


class StatusRepo(IStatusRepo, SQLAlchemyRepo):
    async def get_all(self) -> list[StatusModel]:
        stmt = select(StatusModel)
        result = await self.session.scalars(stmt)
        return result.all()