from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

LETTERBOXD_DATABASE_URL = "postgresql://postgres:ramseyisnice@localhost:5432/boxddb"

engine = create_engine(LETTERBOXD_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
