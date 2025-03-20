from typing import Protocol

from sqlalchemy.orm import registry
from attr import define, field

entity = define(slots=False, kw_only=True)

mapper_registry = registry()


class IUoW(Protocol):
    async def commit(self) -> None:
        ...

    async def rollback(self) -> None:
        ...
