import pandas as pd

from MySQLdb import Connection


def read_label_and_created_at_and_e_mail(connect: Connection):
    cursor = connect.cursor()
    cursor.execute('''select
        archives.id,
        label,
        created_at,
        e_mail
    from archives''')
    fetched_all = cursor.fetchall()

    return fetched_all

def update_posts(connect: Connection, posts: pd.DataFrame):
    cursor = connect.cursor()
    cursor.execute('delete from posts')
    for post in posts.values:
        id = post[0]
        cursor.execute(f'''insert into posts(id) values (
            {id}
        )''')
    
    connect.commit()

def read_label_and_scale_and_reactions(connect: Connection):
    cursor = connect.cursor()
    cursor.execute('''select
        reactions.id,
        label,
        scale,
        sum(thumbsup),
        sum(heart),
        sum(smile),
        sum(astonished)
    from reactions inner join archives on reactions.id=archives.id
    where reactions.id in (select id from posts)
    group by reactions.id''')
    fetched_all = cursor.fetchall()

    return fetched_all

def update_trends(connect: Connection, trends: pd.DataFrame):
    cursor = connect.cursor()
    cursor.execute('''delete from trends''')
    for trend in trends.values:
        id = trend[0]
        thumbsup = trend[1]
        heart = trend[2]
        smile = trend[3]
        astonished = trend[4]
        cursor.execute(f'''insert into trends(id, thumbsup, heart, smile, astonished) values (
            {id},
            {thumbsup},
            {heart},
            {smile},
            {astonished}
        )''')
    connect.commit()