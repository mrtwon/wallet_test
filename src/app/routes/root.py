from fastapi import APIRouter
from src.app.routes.v1.base import v1_router

root_router = APIRouter(prefix='/api')
root_router.include_router(v1_router)
