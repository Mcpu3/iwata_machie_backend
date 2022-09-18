from MySQLdb import Connection


def read_archive_by_id(connect: Connection, id: int):
    cursor = connect.cursor()
    cursor.execute(f'''select
        id,
        body,
        scale,
        reaction_thumbsup,
        reaction_heart,
        reaction_smile,
        reaction_astonished,
        rank_highest_thumbsup,
        rank_highest_heart,
        rank_highest_smile,
        rank_highest_astonished,
        date_and_time,
        ip_address
    from archives_mock
    where id={id}''')
    fetched = cursor.fetchone()

    return fetched

def read_archives(connect: Connection):
    cursor = connect.cursor()
    cursor.execute('''select
        id,
        body,
        scale,
        reaction_thumbsup,
        reaction_heart,
        reaction_smile,
        reaction_astonished,
        rank_highest_thumbsup,
        rank_highest_heart,
        rank_highest_smile,
        rank_highest_astonished,
        date_and_time,
        ip_address
    from archives_mock''')
    fetched_all = cursor.fetchall()

    return fetched_all

def read_archives_by_date_and_time(connect: Connection, date_and_time: str):
    cursor = connect.cursor()
    cursor.execute(f'''select
        id,
        body,
        scale,
        reaction_thumbsup,
        reaction_heart,
        reaction_smile,
        reaction_astonished,
        rank_highest_thumbsup,
        rank_highest_heart,
        rank_highest_smile,
        rank_highest_astonished,
        date_and_time,
        ip_address
    from archives_mock
    where date_and_time>="{date_and_time}"''')
    fetched_all = cursor.fetchall()

    return fetched_all

def read_archives_by_ip_address(connect: Connection, ip_address: str):
    cursor = connect.cursor()
    cursor.execute(f'''select
        id,
        body,
        scale,
        reaction_thumbsup,
        reaction_heart,
        reaction_smile,
        reaction_astonished,
        rank_highest_thumbsup,
        rank_highest_heart,
        rank_highest_smile,
        rank_highest_astonished,
        date_and_time,
        ip_address
    from archives_mock
    where ip_address="{ip_address}"''')
    fetched_all = cursor.fetchall()

    return fetched_all

def read_post_by_id(connect: Connection, id: int):
    cursor = connect.cursor()
    cursor.execute(f'''select
        id,
        body,
        scale,
        reaction_thumbsup,
        reaction_heart,
        reaction_smile,
        reaction_astonished,
        rank_highest_thumbsup,
        rank_highest_heart,
        rank_highest_smile,
        rank_highest_astonished,
        date_and_time,
        ip_address
    from archives_mock
    where id in (select id from posts_mock where id={id})''')
    fetched = cursor.fetchone()

    return fetched

def read_posts(connect: Connection):
    cursor = connect.cursor()
    cursor.execute('''select
        id,
        body,
        scale,
        reaction_thumbsup,
        reaction_heart,
        reaction_smile,
        reaction_astonished,
        rank_highest_thumbsup,
        rank_highest_heart,
        rank_highest_smile,
        rank_highest_astonished,
        date_and_time,
        ip_address
    from archives_mock
    where id in (select id from posts_mock)''')
    fetched_all = cursor.fetchall()

    return fetched_all

def read_posts_by_ip_address(connect: Connection, ip_address: str):
    cursor = connect.cursor()
    cursor.execute(f'''select
        id,
        body,
        scale,
        reaction_thumbsup,
        reaction_heart,
        reaction_smile,
        reaction_astonished,
        rank_highest_thumbsup,
        rank_highest_heart,
        rank_highest_smile,
        rank_highest_astonished,
        date_and_time,
        ip_address
    from archives_mock
    where id in (select id from posts_mock) and ip_address="{ip_address}"''')
    fetched_all = cursor.fetchall()

    return fetched_all

def read_trend_by_id(connect: Connection, id: int):
    cursor = connect.cursor()
    cursor.execute(f'''select
        archives_mock.id,
        rank_thumbsup,
        rank_heart,
        rank_smile,
        rank_astonished
    from archives_mock inner join trends_mock on archives_mock.id=trends_mock.id
    where archives_mock.id in (select id from archives_mock where id={id})''')
    fetched = cursor.fetchone()

    return fetched

def read_trends(connect: Connection):
    cursor = connect.cursor()
    cursor.execute('''select
        archives_mock.id,
        rank_thumbsup,
        rank_heart,
        rank_smile,
        rank_astonished
    from archives_mock inner join trends_mock on archives_mock.id=trends_mock.id''')
    fetched_all = cursor.fetchall()

    return fetched_all

def read_trends_by_scale(connect: Connection, scale: int):
    cursor = connect.cursor()
    cursor.execute(f'''select
        archives_mock.id,
        rank_thumbsup,
        rank_heart,
        rank_smile,
        rank_astonished
    from archives_mock inner join trends_mock on archives_mock.id=trends_mock.id and archives_mock.scale={scale}''')
    fetched_all = cursor.fetchall()

    return fetched_all

def read_trends_by_scale_and_rank(connect: Connection, scale: int, rank: int, reaction: str):
    cursor = connect.cursor()
    cursor.execute(f'''select
        archives_mock.id,
        rank_thumbsup,
        rank_heart,
        rank_smile,
        rank_astonished
    from archives_mock inner join trends_mock on archives_mock.id=trends_mock.id and archives_mock.scale={scale}
    where rank_{reaction}<={rank}''')
    fetched_all = cursor.fetchall()

    return fetched_all