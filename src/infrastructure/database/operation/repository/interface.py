from typing import Protocol

from src.infrastructure.database.operation.model import OperationModel


class IOperationRepo(Protocol):
    async def get_all(self) -> list[OperationModel]:
        ...