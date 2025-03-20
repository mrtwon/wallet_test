from fastapi import FastAPI

from src.app.di.base import di_all
from src.app.di.setup import di_setup
from src.app.middleware.exception_handler import add_application_exception_handler
from src.app.routes.root import root_router

import src.infrastructure.database.wallet.table
import src.infrastructure.database.status.table
import src.infrastructure.database.wallet_operation.table
import src.infrastructure.database.operation.table

app = FastAPI()
di_all(app)
app.include_router(root_router)
add_application_exception_handler(app)
