from fastapi import APIRouter
from .operation import operation_router
from .status import router_status
from .wallet import wallet_router

v1_router = APIRouter(prefix='/v1')

v1_router.include_router(wallet_router)
v1_router.include_router(operation_router)
v1_router.include_router(router_status)
