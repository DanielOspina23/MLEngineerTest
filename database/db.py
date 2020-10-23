from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import settings


connection_uri = "postgres+psycopg2://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DATABASE}".format(
    PG_USER=settings.PG_USER,
    PG_PASSWORD=settings.PG_PASSWORD,
    PG_HOST=settings.PG_HOST,
    PG_PORT=settings.PG_PORT,
    PG_DATABASE=settings.PG_DATABASE
)

engine = create_engine(connection_uri, pool_pre_ping=True)

# Declaring the mapping
Base = declarative_base(bind=engine)


def create_session(engine_object: object):
    session_factory = scoped_session(sessionmaker(bind=engine_object))
    return session_factory
