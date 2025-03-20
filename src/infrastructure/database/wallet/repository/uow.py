from src.infrastructure.database.base import IUoW
from src.infrastructure.database.wallet.repository.interface import IWalletRepo


class IWalletUOW(IUoW):
    wallet: IWalletRepo
