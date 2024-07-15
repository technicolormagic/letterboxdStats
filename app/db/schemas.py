from pydantic import BaseModel
import datetime

class MovieBase(BaseModel):
    title: str
    releaseDate: datetime.date
    country: str
    language: str
    link: str

class MovieCreate(MovieBase):
    pass

class MovieRead(MovieBase):
    id: int

class JobsBase(BaseModel):
    job: str

class JobsCreate(JobsBase):
    pass

class JobsRead(JobsBase):
    id: int

class PeopleBase(BaseModel):
    name: str
    jobs: list[JobsRead] = []

    class Config:
        from_attributes = True

class PeopleCreate(PeopleBase):
    pass

class PeopleRead(PeopleBase):
    id: int

class MoviePeopleBase(BaseModel):
    pass

class MoviePeopleCreate(MoviePeopleBase):
    pass

class MoviePeopleRead(MoviePeopleBase):
    pass

class WatchedBase(BaseModel):
    movieId: int

class WatchedCreate(WatchedBase):
    pass

class WatchedRead(WatchedBase):
    id: int

class TagsBase(BaseModel):
    tag: str

class TagsCreate(TagsBase):
    pass

class TagsRead(TagsBase):
    id: int

class ReviewsBase(BaseModel):
    movieId: int
    tagId: int
    review: str
    date: datetime.date
    rating: int

class ReviewsCreate(ReviewsBase):
    pass

class ReviewsRead(ReviewsBase):
    id: int
    movie: list[MovieRead]=[]

    class Config:
        from_attributes = True

    tags: list[TagsRead]=[]
    
    class Config:
        from_attributes = True