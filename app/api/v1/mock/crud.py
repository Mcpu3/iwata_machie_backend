from MySQLdb import Connection


def read_post_by_id(connect: Connection, id: int):
    cursor = connect.cursor()
    cursor.execute(f'''select
        id,
        body,
        scale,
        date_and_time
    from archives_mock
    where id in (select id from posts_mock where id={id})''')
    fetched = cursor.fetchone()

    return fetched

def read_posts_by_ip_address(connect: Connection, ip_address: str):
    cursor = connect.cursor()
    cursor.execute(f'''select
        id,
        body,
        scale,
        date_and_time
    from archives_mock
    where id in (select id from posts_mock) and ip_address="{ip_address}"''')
    fetched_all = cursor.fetchall()

    return fetched_all

def read_reaction_by_id(connect: Connection, id: int):
    cursor = connect.cursor()
    cursor.execute(f'''select
        id,
        sum(thumbsup),
        sum(heart),
        sum(smile),
        sum(astonished)
    from reactions_mock
    where id={id}
    ''')
    fetched = cursor.fetchone()

    return fetched

def read_reaction_by_id_and_ip_address(connect: Connection, id: int, ip_address: str):
    cursor = connect.cursor()
    cursor.execute(f'''select
        id,
        thumbsup,
        heart,
        smile,
        astonished
    from reactions_mock
    where id={id} and ip_address="{ip_address}"''')
    fetched = cursor.fetchone()

    return fetched

def read_reactions_by_ip_address(connect: Connection, ip_address: str):
    cursor = connect.cursor()
    cursor.execute(f'''select
        id,
        thumbsup,
        heart,
        smile,
        astonished
    from reactions_mock
    where ip_address="{ip_address}"
    ''')
    fetched_all = cursor.fetchall()

    return fetched_all

def read_trend_by_id(connect: Connection, id: int):
    cursor = connect.cursor()
    cursor.execute(f'''select
        archives_mock.id,
        thumbsup,
        heart,
        smile,
        astonished
    from archives_mock inner join trends_mock on archives_mock.id=trends_mock.id
    where archives_mock.id in (select id from archives_mock where id={id})''')
    fetched = cursor.fetchone()

    return fetched

def read_trends_by_scale(connect: Connection, scale: int):
    cursor = connect.cursor()
    cursor.execute(f'''select
        archives_mock.id,
        thumbsup,
        heart,
        smile,
        astonished
    from archives_mock inner join trends_mock on archives_mock.id=trends_mock.id and archives_mock.scale={scale}''')
    fetched_all = cursor.fetchall()

    return fetched_all


def read_archive_by_id(connect: Connection, id: int):
    cursor = connect.cursor()
    cursor.execute(f'''select
        id,
        body,
        scale,
        date_and_time
    from archives_mock
    where id={id}''')
    fetched = cursor.fetchone()

    return fetched

def read_archives_by_ip_address(connect: Connection, ip_address: str):
    cursor = connect.cursor()
    cursor.execute(f'''select
        id,
        body,
        scale,
        date_and_time
    from archives_mock
    where ip_address="{ip_address}"''')
    fetched_all = cursor.fetchall()

    return fetched_all