from typing import Optional

from fastapi import APIRouter
import MySQLdb

from api.v1.mock.schemas import Archive, Archives, Post, Posts, NewPost, Trend, Trends
from api.v1.mock import crud


api_router = APIRouter()
connect = MySQLdb.connect(host='db', user='root', password='password', db='api')

@api_router.get('/archive/{id}/', response_model=Archive)
def get_archive_by_id_mock(id: int) -> Archive:
    fetched = crud.read_archive_by_id(connect, id)
    archive: Archive = {
        'id': fetched[0],
        'body': fetched[1],
        'scale': fetched[2],
        'reaction_thumbsup': fetched[3],
        'reaction_heart': fetched[4],
        'reaction_smile': fetched[5],
        'reaction_astonished': fetched[6],
        'rank_highest_thumbsup': fetched[7],
        'rank_highest_heart': fetched[8],
        'rank_highest_smile': fetched[9],
        'rank_highest_astonished': fetched[10],
        'date_and_time': fetched[11].strftime('%Y-%m-%d %H:%M:%S'),
        'ip_address': fetched[12]
    }

    return archive

@api_router.get('/archives/', response_model=Archives)
def get_archives_mock(date_and_time: Optional[str] = None, ip_address: Optional[str] = None) -> Archives:
    if date_and_time:
        fetched_all = crud.read_archives_by_date_and_time(connect, date_and_time)
    elif ip_address:
        fetched_all = crud.read_archives_by_ip_address(connect, ip_address)
    else:
        fetched_all = crud.read_archives(connect)
    archives = []
    for fetched in fetched_all:
        archive: Archive = {
            'id': fetched[0],
            'body': fetched[1],
            'scale': fetched[2],
            'reaction_thumbsup': fetched[3],
            'reaction_heart': fetched[4],
            'reaction_smile': fetched[5],
            'reaction_astonished': fetched[6],
            'rank_highest_thumbsup': fetched[7],
            'rank_highest_heart': fetched[8],
            'rank_highest_smile': fetched[9],
            'rank_highest_astonished': fetched[10],
            'date_and_time': fetched[11].strftime('%Y-%m-%d %H:%M:%S'),
            'ip_address': fetched[12]
        }
        archives.append(archive)
    archives: Archives = {
        'archives': archives
    }

    return archives

@api_router.get('/post/{id}/', response_model=Post)
def get_post_by_id_mock(id: int) -> Post:
    fetched = crud.read_post_by_id(connect, id)
    post: Post = {
        'id': fetched[0],
        'body': fetched[1],
        'scale': fetched[2],
        'reaction_thumbsup': fetched[3],
        'reaction_heart': fetched[4],
        'reaction_smile': fetched[5],
        'reaction_astonished': fetched[6],
        'rank_highest_thumbsup': fetched[7],
        'rank_highest_heart': fetched[8],
        'rank_highest_smile': fetched[9],
        'rank_highest_astonished': fetched[10],
        'date_and_time': fetched[11].strftime('%Y-%m-%d %H:%M:%S'),
        'ip_address': fetched[12]
    }

    return post

@api_router.get('/posts/', response_model=Posts)
def get_posts_mock(ip_address: Optional[str] = None) -> Posts:
    if ip_address:
        fetched_all = crud.read_posts_by_ip_address(connect, ip_address)
    else:
        fetched_all = crud.read_posts(connect)
    posts = []
    for fetched in fetched_all:
        post: Post = {
            'id': fetched[0],
            'body': fetched[1],
            'scale': fetched[2],
            'reaction_thumbsup': fetched[3],
            'reaction_heart': fetched[4],
            'reaction_smile': fetched[5],
            'reaction_astonished': fetched[6],
            'rank_highest_thumbsup': fetched[7],
            'rank_highest_heart': fetched[8],
            'rank_highest_smile': fetched[9],
            'rank_highest_astonished': fetched[10],
            'date_and_time': fetched[11].strftime('%Y-%m-%d %H:%M:%S'),
            'ip_address': fetched[12]
        }
        posts.append(post)
    posts: Posts = {
        'posts': posts
    }

    return posts

@api_router.post('/new_post/', response_model=NewPost)
def post_new_post_mock(new_post: NewPost) -> NewPost:
    
    return new_post

@api_router.get('/trend/{id}/', response_model=Trend)
def get_trend_by_id_mock(id: int) -> Trend:
    fetched = crud.read_trend_by_id(connect, id)
    trend: Trend = {
        'id': fetched[0],
        'rank_thumbsup': fetched[1],
        'rank_heart': fetched[2],
        'rank_smile': fetched[3],
        'rank_astonished': fetched[4]
    }

    return trend

@api_router.get('/trends/', response_model=Trends)
def get_trends_mock() -> Trends:
    fetched_all = crud.read_trends(connect)
    trends = []
    for fetched in fetched_all:
        trend: Trend = {
            'id': fetched[0],
            'rank_thumbsup': fetched[1],
            'rank_heart': fetched[2],
            'rank_smile': fetched[3],
            'rank_astonished': fetched[4]
        }
        trends.append(trend)
    trends: Trends = {
        'trends': trends
    }

    return trends

@api_router.get('/trends/{scale}/', response_model=Trends)
def get_trends_by_scale_mock(scale: int, rank: Optional[int] = None, reaction: Optional[str] = None) -> Trends:
    if rank and reaction:
        fetched_all = crud.read_trends_by_scale_and_rank(connect, scale, rank, reaction)
    else:
        fetched_all = crud.read_trends_by_scale(connect, scale)
    trends = []
    for fetched in fetched_all:
        trend: Trend = {
            'id': fetched[0],
            'rank_thumbsup': fetched[1],
            'rank_heart': fetched[2],
            'rank_smile': fetched[3],
            'rank_astonished': fetched[4]
        }
        trends.append(trend)
    trends: Trends = {
        'trends': trends
    }

    return trends