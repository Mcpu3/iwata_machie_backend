from pydantic import BaseModel


class Post(BaseModel):
    id: int
    body: str
    label: int
    scale: int
    date_and_time: str


class Posts(BaseModel):
    posts: list[Post]


class NewPost(BaseModel):
    body: str
    label: int
    scale: int
    e_mail: str


class Reaction(BaseModel):
    id: int
    thumbsup: int
    heart: int
    smile: int
    astonished: int


class Reactions(BaseModel):
    reactions: list[Reaction]


class NewReaction(BaseModel):
    thumbsup: int
    heart: int
    smile: int
    astonished: int
    e_mail: str


class Trend(BaseModel):
    id: int
    thumbsup: int
    heart: int
    smile: int
    astonished: int


class Trends(BaseModel):
    trends: list[Trend]


class Archive(BaseModel):
    id: int
    body: str
    label: int
    scale: int
    date_and_time: str


class Archives(BaseModel):
    archives: list[Archive]