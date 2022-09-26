from pydantic import BaseModel

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