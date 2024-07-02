from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#LETTERBOXD_DATABASE_URL = "something goes here"

#engine = create_engine(LETTERBOXD_DATABASE_URL)

#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
