from typing import Annotated
import os

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=create_engine(os.environ.get("URL")))


async def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_session_depend = Annotated[Session, Depends(get_db)]