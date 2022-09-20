from datetime import datetime
from typing import Optional

from fastapi import APIRouter
import MySQLdb

from api.v1 import schemas
from api.v1 import crud


api_router = APIRouter()
connect = MySQLdb.connect(host='db', user='root', password='password', db='api')


@api_router.get('/post/', response_model=schemas.Post)
def get_post() -> schemas.Post:
    fetched = crud.read_post(connect)
    post: schemas.Post = {
        'id': fetched[0],
        'body': fetched[1],
        'label': fetched[2],
        'scale': fetched[3],
        'created_at': fetched[4].strftime('%Y-%m-%d %H:%M:%S')
    }

    return post

@api_router.get('/post/{id}/', response_model=schemas.Post)
def get_post_by_id(id: int) -> schemas.Post:
    fetched = crud.read_post_by_id(connect, id)
    post: schemas.Post = {
        'id': fetched[0],
        'body': fetched[1],
        'label': fetched[2],
        'scale': fetched[3],
        'created_at': fetched[4].strftime('%Y-%m-%d %H:%M:%S')
    }

    return post

@api_router.get('/posts/', response_model=schemas.Posts)
def get_posts_by_e_mail(e_mail: str) -> schemas.Posts:
    fetched_all = crud.read_posts_by_e_mail(connect, e_mail)
    posts = []
    for fetched in fetched_all:
        post: schemas.Post = {
            'id': fetched[0],
            'body': fetched[1],
            'label': fetched[2],
            'scale': fetched[3],
            'created_at': fetched[4].strftime('%Y-%m-%d %H:%M:%S')
        }
        posts.append(post)
    posts: schemas.Posts = {
        'posts': posts
    }

    return posts

@api_router.post('/new_post/', response_model=schemas.NewPost)
def post_new_post(new_post: schemas.NewPost) -> schemas.NewPost:
    body = new_post.body
    label = new_post.label
    scale = new_post.scale
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    e_mail = new_post.e_mail
    crud.create_new_post(connect, body, label, scale, created_at, e_mail)

    return new_post

@api_router.get('/post/{id}/reaction/', response_model=schemas.Reaction)
def get_reaction_by_id_and_e_mail(id: int, e_mail: Optional[str] = None) -> schemas.Reaction:
    if e_mail:
        fetched = crud.read_reaction_by_id_and_e_mail(connect, id, e_mail)
    else:
        fetched = crud.read_reaction_by_id(connect, id)
    reaction: schemas.Reaction = {
        'id': fetched[0],
        'thumbsup': fetched[1],
        'heart': fetched[2],
        'smile': fetched[3],
        'astonished': fetched[4]
    }

    return reaction

@api_router.get('/reactions/', response_model=schemas.Reactions)
def get_reactions_by_e_mail(e_mail: str) -> schemas.Reactions:
    fetched_all = crud.read_reactions_by_e_mail(connect, e_mail)
    reactions = []
    for fetched in fetched_all:
        reaction: schemas.Reaction = {
            'id': fetched[0],
            'thumbsup': fetched[1],
            'heart': fetched[2],
            'smile': fetched[3],
            'astonished': fetched[4]
        }
        reactions.append(reaction)
    reactions: schemas.Reactions = {
        'reactions': reactions
    }

    return reactions

@api_router.post('/post/{id}/new_reaction/', response_model=schemas.NewReaction)
def post_new_reaction(id: int, new_reaction: schemas.NewReaction) -> schemas.NewReaction:
    thumbsup = new_reaction.thumbsup
    heart = new_reaction.heart
    smile = new_reaction.smile
    astonished = new_reaction.astonished
    e_mail = new_reaction.e_mail
    crud.create_new_reaction(connect, id, thumbsup, heart, smile, astonished, e_mail)

    return new_reaction

@api_router.get('/post/{id}/trend/', response_model=schemas.Trend)
def get_trend_by_id(id: int) -> schemas.Trend:
    fetched = crud.read_trend_by_id(connect, id)
    trend: schemas.Trend = {
        'id': fetched[0],
        'thumbsup': fetched[1],
        'heart': fetched[2],
        'smile': fetched[3],
        'astonished': fetched[4]
    }

    return trend

@api_router.get('/trends/', response_model=schemas.Trends)
def get_trends_by_label_and_scale(label: int, scale: int) -> schemas.Trends:
    fetched_all = crud.read_trends_by_label_and_scale(connect, label, scale)
    trends = []
    for fetched in fetched_all:
        trend: schemas.Trend = {
            'id': fetched[0],
            'thumbsup': fetched[1],
            'heart': fetched[2],
            'smile': fetched[3],
            'astonished': fetched[4]
        }
        trends.append(trend)
    trends: schemas.Trends = {
        'trends': trends
    }

    return trends

@api_router.get('/archive/{id}/', response_model=schemas.Archive)
def get_archive_by_id(id: int) -> schemas.Archive:
    fetched = crud.read_archive_by_id(connect, id)
    archive: schemas.Archive = {
        'id': fetched[0],
        'body': fetched[1],
        'label': fetched[2],
        'scale': fetched[3],
        'created_at': fetched[4].strftime('%Y-%m-%d %H:%M:%S')
    }

    return archive

@api_router.get('/archives/', response_model=schemas.Archives)
def get_archives_by_e_mail(e_mail: str) -> schemas.Archives:
    fetched_all = crud.read_archives_by_e_mail(connect, e_mail)
    archives = []
    for fetched in fetched_all:
        archive: schemas.Archive = {
            'id': fetched[0],
            'body': fetched[1],
            'label': fetched[2],
            'scale': fetched[3],
            'created_at': fetched[4].strftime('%Y-%m-%d %H:%M:%S')
        }
        archives.append(archive)
    archives: schemas.Archives = {
        'archives': archives
    }

    return archives