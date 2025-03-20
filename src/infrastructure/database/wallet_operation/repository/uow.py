from src.infrastructure.database.base import IUoW
from src.infrastructure.database.wallet_operation.repository.interface import IWalletOperationRepo


class IWalletOperationUOW(IUoW):
    wallet_operation: IWalletOperationRepo
