from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlraw

connstr = "postgresql://postgres:postgres@localhost:5432/ shopping_centre"
engine = create_engine(connstr, echo=False)
conn = engine.connect()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

