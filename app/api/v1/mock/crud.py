from MySQLdb import Connection


def read_post_by_id(connect: Connection, id: int):
    cursor = connect.cursor()
    cursor.execute(f'''select
        id,
        body,
        label,
        scale,
        created_at
    from archives_mock
    where id in (select id from posts_mock where id={id})''')
    fetched = cursor.fetchone()

    return fetched

def read_posts_by_e_mail(connect: Connection, e_mail: str):
    cursor = connect.cursor()
    cursor.execute(f'''select
        id,
        body,
        label,
        scale,
        created_at
    from archives_mock
    where id in (select id from posts_mock) and e_mail="{e_mail}"''')
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

def read_reaction_by_id_and_e_mail(connect: Connection, id: int, e_mail: str):
    cursor = connect.cursor()
    cursor.execute(f'''select
        id,
        thumbsup,
        heart,
        smile,
        astonished
    from reactions_mock
    where id={id} and e_mail="{e_mail}"''')
    fetched = cursor.fetchone()

    return fetched

def read_reactions_by_e_mail(connect: Connection, e_mail: str):
    cursor = connect.cursor()
    cursor.execute(f'''select
        id,
        thumbsup,
        heart,
        smile,
        astonished
    from reactions_mock
    where e_mail="{e_mail}"
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

def read_trends_by_label_and_scale(connect: Connection, label: int, scale: int):
    cursor = connect.cursor()
    cursor.execute(f'''select
        archives_mock.id,
        thumbsup,
        heart,
        smile,
        astonished
    from archives_mock inner join trends_mock on archives_mock.id=trends_mock.id and archives_mock.label={label} and archives_mock.scale={scale}''')
    fetched_all = cursor.fetchall()

    return fetched_all


def read_archive_by_id(connect: Connection, id: int):
    cursor = connect.cursor()
    cursor.execute(f'''select
        id,
        body,
        label,
        scale,
        created_at
    from archives_mock
    where id={id}''')
    fetched = cursor.fetchone()

    return fetched

def read_archives_by_e_mail(connect: Connection, e_mail: str):
    cursor = connect.cursor()
    cursor.execute(f'''select
        id,
        body,
        label,
        scale,
        created_at
    from archives_mock
    where e_mail="{e_mail}"''')
    fetched_all = cursor.fetchall()

    return fetched_all