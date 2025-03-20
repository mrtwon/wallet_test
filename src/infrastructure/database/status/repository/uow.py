from src.infrastructure.database.status.repository.interface import IStatusRepo
from src.infrastructure.database.base import IUoW



class IStatusUOW(IUoW):
    status: IStatusRepo