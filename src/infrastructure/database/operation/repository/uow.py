from src.infrastructure.database.operation.repository.interface import IOperationRepo
from src.infrastructure.database.base import IUoW


class IOperationUOW(IUoW):
    operation: IOperationRepo