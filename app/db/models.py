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
    # example: items = relationship("Item", back_populates="owner")
    peopleR0 = relationship("People", back_populates="moviesR0")
    reviewsR0 = relationship("Reviews", back_populates="moviesR1")

class People(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    #relationships
    moviesR0 = relationship("Movies", back_populates="peopleR0")
    jobsR0 = relationship("Jobs", back_populates="peopleR1")

class Jobs(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    jobTitle= Column(String)

    #relationships
    peopleR1 = relationship("People", back_populates="jobsR0")

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
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    tag = Column(String)

    #relationships
    reviewsR1 = relationship("Reviews", back_populates="tagsR0")

class Reviews(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    movieId = Column(Integer, ForeignKey(Movies.id))
    tagId = Column(Integer, ForeignKey(Tags.id))
    review = Column(String)
    date = Column(Date)
    rating = Column(Integer)

    #relationships
    moviesR1 = relationship("Movies", back_populates="reviewsR0")
    tagsR0 = relationship("Tags", back_populates="reviewsR1")
