from MySQLdb import Connection


def read_post(connect: Connection):
    cursor = connect.cursor()
    cursor.execute('''select
        id,
        body,
        label,
        scale,
        created_at
    from archives
    where id in (select id from (select id from posts order by rand() limit 1) as posts_1)''')
    fetched = cursor.fetchone()

    return fetched

def read_post_by_id(connect: Connection, id: int):
    cursor = connect.cursor()
    cursor.execute(f'''select
        id,
        body,
        label,
        scale,
        created_at
    from archives
    where id in (select id from posts where id={id})''')
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
    from archives
    where id in (select id from posts) and e_mail="{e_mail}"''')
    fetched_all = cursor.fetchall()

    return fetched_all

def create_new_post(connect: Connection, body: str, label: int, scale: int, created_at: str, e_mail: str):
    cursor = connect.cursor()
    cursor.execute(f'''insert into archives(body, label, scale, created_at, e_mail) values (
        "{body}",
        {label},
        {scale},
        "{created_at}",
        "{e_mail}"
    )''')
    connect.commit()

def read_reaction_by_id(connect: Connection, id: int):
    cursor = connect.cursor()
    cursor.execute(f'''select
        id,
        sum(thumbsup),
        sum(heart),
        sum(smile),
        sum(astonished)
    from reactions
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
    from reactions
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
    from reactions
    where e_mail="{e_mail}"
    ''')
    fetched_all = cursor.fetchall()

    return fetched_all

def create_new_reaction(connect: Connection, id: int, thumbsup: int, heart: int, smile: int, astonished: int, e_mail: str):
    cursor = connect.cursor()
    cursor.execute(f'''replace into reactions(id, thumbsup, heart, smile, astonished, e_mail) values (
        {id},
        {thumbsup},
        {heart},
        {smile},
        {astonished},
        "{e_mail}"
    )''')
    connect.commit()

def read_trend_by_id(connect: Connection, id: int):
    cursor = connect.cursor()
    cursor.execute(f'''select
        archives.id,
        thumbsup,
        heart,
        smile,
        astonished
    from archives inner join trends on archives.id=trends.id
    where archives.id in (select id from archives where id={id})''')
    fetched = cursor.fetchone()

    return fetched

def read_trends_by_label_and_scale(connect: Connection, label: int, scale: int):
    cursor = connect.cursor()
    cursor.execute(f'''select
        archives.id,
        thumbsup,
        heart,
        smile,
        astonished
    from archives inner join trends on archives.id=trends.id and archives.label={label} and archives.scale={scale}''')
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
    from archives
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
    from archives
    where e_mail="{e_mail}"''')
    fetched_all = cursor.fetchall()

    return fetched_all