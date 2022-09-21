from time import sleep
from datetime import datetime, timedelta

import schedule
import MySQLdb
from MySQLdb import Connection
import pandas as pd

import crud


def update_posts(connect: Connection):
    fetched_all = crud.read_label_and_created_at_and_e_mail(connect)
    posts = pd.DataFrame(fetched_all, columns=['id', 'label', 'created_at', 'e_mail'])
    created_at = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
    posts = posts[posts.created_at >= created_at]
    posts = posts.sort_values('created_at').drop_duplicates(subset=['label', 'e_mail'], keep='last')
    crud.update_posts(connect, posts)

def update_trends(connect: Connection):
    fetched_all = crud.read_label_and_scale_and_reactions(connect)
    trends = pd.DataFrame(fetched_all, columns=['id', 'label', 'scale', 'thumbsup', 'heart', 'smile', 'astonished'])
    trends = trends.loc[:, ['id']].join(trends.loc[:, ['label', 'scale', 'thumbsup', 'heart', 'smile', 'astonished']].groupby(['label', 'scale']).rank('min'))
    crud.update_trends(connect, trends)

if __name__ == '__main__':
    connect = MySQLdb.connect(host='db', user='root', password='password', db='api')
    schedule.every().seconds.do(update_posts, connect)
    schedule.every().seconds.do(update_trends, connect)
    while True:
        schedule.run_pending()
        sleep(1)