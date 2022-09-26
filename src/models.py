from sqlalchemy import Column, Integer, String, ForeignKey, Date
from .database import Base
from sqlalchemy.orm import relationship


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    image_url = Column(String)
    description = Column(String)
    short_description = Column(String)
    organized_by = Column(String)
    location = Column(String)
    date = Column(Date)


class Sponsor(Base):
    __tablename__ = 'sponsors'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    # image_url = Column(String)
    # description = Column(String)
    # short_description = Column(String)
    # headquarter_location = Column(String)
    # website_url = Column(String)
    # facebook_url = Column(String)
    # twitter_url = Column(String)
    # instagram_url = Column(String)
