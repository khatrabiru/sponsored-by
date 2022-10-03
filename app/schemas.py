from sqlite3 import Date
from typing import List
from pydantic import BaseModel


class Event(BaseModel):
    name: str
    image_url: str
    description: str
    short_description: str
    organized_by: str
    location: str
    category: str
    date: Date
    sponsors: list[int]


class ShowEvent(Event):
    id: int
    class Config():
        orm_mode = True


class Sponsor(BaseModel):
    name: str
    image_url: str
    description: str
    short_description: str
    headquarter_location: str
    website_url: str
    facebook_url: str
    twitter_url: str
    instagram_url: str
    events: list[int]


class ShowSponsor(Sponsor):
    id: int
    class Config():
        orm_mode = True
