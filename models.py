from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Movies(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    releaseData = Column(Date)
    country = Column(String)
    language = Column(String)
    link = Column(String, unique=True)

    #relationships

class People(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    #relationships

class Jobs(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    jobTitle= Column(String)

    #relationships

class MoviesPeople(Base):
    __tablename__ = "moviesPeople"

    id = Column(Integer, primary_key=True)
    movieId = Column(Integer, ForeignKey(Movies.id))
    personId = Column(Integer, ForeignKey(People.id))
    jobId = Column(Integer, ForeignKey(Jobs.id))

    #relationships

class Watched(Base):
    __tablename__ = "watched"

    id = Column(Integer, primary_key=True)
    movieId = Column(Integer, ForeignKey(Movies.id))

    #relationships

class Tags(Base):
    _tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    tag = Column(String)

    #relationships

class Reviews(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    movieId = Column(Integer, ForeignKey(Movies.id))
    tagId = Column(Integer, ForeignKey(Tag.id))
    review = Column(String)
    date = Column(Date)
    rating = Column(Integer)

    #relationships