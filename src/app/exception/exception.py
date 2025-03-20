from src.app.exception.base import AppBaseException


class PropertyNotFoundException(AppBaseException):
    detail = 'property not found'
    status = 400


class WalletNotFound(AppBaseException):
    detail = 'wallet not found'
    status = 404


class NotEnoughMoneyException(AppBaseException):
    detail = 'not enough money for transaction'
    status = 403


class UnknownMoneyOperationException(AppBaseException):
    detail = 'unknown money operation'
    status = 400
