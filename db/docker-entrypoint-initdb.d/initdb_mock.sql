use api;
create table archives_mock
(
    id int auto_increment,
    body varchar(1024),
    scale int,
    date_and_time timestamp,
    ip_address varchar(1024),
    primary key (id)
);
insert into archives_mock(body, scale, date_and_time, ip_address) values
(
    "hello",
    1,
    "2022-09-20 06:00:00",
    "192.168.0.1"
);
insert into archives_mock(body, scale, date_and_time, ip_address) values
(
    "world",
    2,
    "2022-09-20 18:00:00",
    "192.168.0.2"
);
insert into archives_mock(body, scale, date_and_time, ip_address) values
(
    "こんにちは",
    3,
    "2022-09-21 06:00:00",
    "192.168.0.1"
);
insert into archives_mock(body, scale, date_and_time, ip_address) values
(
    "世界",
    1,
    "2022-09-21 18:00:00",
    "192.168.0.2"
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
create table reactions_mock
(
    id int,
    thumbsup int,
    heart int,
    smile int,
    astonished int,
    ip_address varchar(1024),
    foreign key (id) references archives_mock(id)
);
insert into reactions_mock values
(
    1,
    1,
    0,
    0,
    0,
    "192.168.0.1"
);
insert into reactions_mock values
(
    2,
    0,
    1,
    0,
    0,
    "192.168.0.2"
);
insert into reactions_mock values
(
    3,
    0,
    0,
    1,
    0,
    "192.168.0.3"
);
insert into reactions_mock values
(
    1,
    0,
    0,
    0,
    1,
    "192.168.0.4"
);
create table trends_mock
(
    id int,
    thumbsup int,
    heart int,
    smile int,
    astonished int,
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