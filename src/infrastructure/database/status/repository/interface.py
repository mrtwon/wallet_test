from typing import Protocol

from src.infrastructure.database.status.model import StatusModel


class IStatusRepo(Protocol):
    async def get_all(self) -> list[StatusModel]:
        ...