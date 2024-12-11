from sqlalchemy import create_engine

from db.models import Base


engine = create_engine('postgresql://admin:admin@postgres/mydatabase')

Base.metadata.create_all(engine)

