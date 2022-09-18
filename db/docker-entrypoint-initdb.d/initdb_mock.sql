use api;
create table archives_mock
(
    id int auto_increment,
    body varchar(1024),
    scale int,
    reaction_thumbsup int,
    reaction_heart int,
    reaction_smile int,
    reaction_astonished int,
    rank_highest_thumbsup int,
    rank_highest_heart int,
    rank_highest_smile int,
    rank_highest_astonished int,
    date_and_time timestamp,
    ip_address varchar(1024),
    primary key (id)
);
insert into archives_mock(body, scale, reaction_thumbsup, reaction_heart, reaction_smile, reaction_astonished, rank_highest_thumbsup, rank_highest_heart, rank_highest_smile, rank_highest_astonished, date_and_time, ip_address) values
(
    "hello",
    1,
    0,
    1,
    2,
    3,
    1,
    2,
    3,
    4,
    "2022-09-20 06:00:00",
    "192.168.0.1"
);
insert into archives_mock(body, scale, reaction_thumbsup, reaction_heart, reaction_smile, reaction_astonished, rank_highest_thumbsup, rank_highest_heart, rank_highest_smile, rank_highest_astonished, date_and_time, ip_address) values
(
    "world",
    2,
    1,
    2,
    3,
    0,
    2,
    3,
    4,
    1,
    "2022-09-20 18:00:00",
    "192.168.0.2"
);
insert into archives_mock(body, scale, reaction_thumbsup, reaction_heart, reaction_smile, reaction_astonished, rank_highest_thumbsup, rank_highest_heart, rank_highest_smile, rank_highest_astonished, date_and_time, ip_address) values
(
    "こんにちは",
    3,
    2,
    3,
    0,
    1,
    3,
    4,
    1,
    2,
    "2022-09-21 06:00:00",
    "192.168.0.3"
);
insert into archives_mock(body, scale, reaction_thumbsup, reaction_heart, reaction_smile, reaction_astonished, rank_highest_thumbsup, rank_highest_heart, rank_highest_smile, rank_highest_astonished, date_and_time, ip_address) values
(
    "世界",
    1,
    3,
    0,
    1,
    2,
    4,
    1,
    2,
    3,
    "2022-09-21 18:00:00",
    "192.168.0.1"
);
create table posts_mock
(
    id int,
    foreign key (id) references archives_mock(id)
);
insert into posts_mock values
(
    1
);
insert into posts_mock values
(
    2
);
create table trends_mock
(
    id int,
    rank_thumbsup int,
    rank_heart int,
    rank_smile int,
    rank_astonished int,
    foreign key (id) references archives_mock(id)
);
insert into trends_mock values
(
    1,
    1,
    2,
    3,
    4
);
insert into trends_mock values
(
    2,
    4,
    3,
    2,
    1
);