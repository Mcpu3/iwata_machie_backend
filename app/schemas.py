from pydantic import BaseModel


class Archive(BaseModel):
    id: int
    body: str
    scale: int
    reaction_thumbsup: int
    reaction_heart: int
    reaction_smile: int
    reaction_astonished: int
    rank_highest_thumbsup: int
    rank_highest_heart: int
    rank_highest_smile: int
    rank_highest_astonished: int
    date_and_time: str
    ip_address: str


class Archives(BaseModel):
    archives: list[Archive]


class Post(BaseModel):
    id: int
    body: str
    scale: int
    reaction_thumbsup: int
    reaction_heart: int
    reaction_smile: int
    reaction_astonished: int
    rank_highest_thumbsup: int
    rank_highest_heart: int
    rank_highest_smile: int
    rank_highest_astonished: int
    date_and_time: str
    ip_address: str


class Posts(BaseModel):
    posts: list[Post]


class NewPost(BaseModel):
    body: str
    scale: int


class Trend(BaseModel):
    id: int
    rank_thumbsup: int
    rank_heart: int
    rank_smile: int
    rank_astonished: int


class Trends(BaseModel):
    trends: list[Trend]