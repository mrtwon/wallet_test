class AppBaseException(Exception):
    detail: str
    status: int