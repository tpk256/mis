from datetime import datetime

from pydantic import BaseModel


class Base(BaseModel):
    id: int
    time_update: datetime | None
    time_created: datetime | None