from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession


class SQLAlchemyRepo:
    def __init__(self, session: AsyncSession) -> Any:
        self.session = session
