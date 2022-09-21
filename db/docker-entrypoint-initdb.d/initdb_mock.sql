use api;
create table archives_mock
(
    id int auto_increment,
    body varchar(1024),
    label int,
    scale int,
    created_at timestamp,
    e_mail varchar(256),
    primary key (id)
);
insert into archives_mock(body, label, scale, created_at, e_mail) values
(
    "hello",
    1,
    1,
    "2022-09-20 06:00:00",
    "abc@email.com"
);
insert into archives_mock(body, label, scale, created_at, e_mail) values
(
    "world",
    2,
    2,
    "2022-09-20 18:00:00",
    "def@email.com"
);
insert into archives_mock(body, label, scale, created_at, e_mail) values
(
    "こんにちは",
    1,
    3,
    "2022-09-21 06:00:00",
    "ghi@email.com"
);
insert into archives_mock(body, label, scale, created_at, e_mail) values
(
    "世界",
    2,
    1,
    "2022-09-21 18:00:00",
    "abc@email.com"
);
create table posts_mock
(
    id int,
    foreign key (id) references archives_mock(id)
);
insert into posts_mock values
(
    3
);
insert into posts_mock values
(
    4
);
create table reactions_mock
(
    id int,
    thumbsup int,
    heart int,
    smile int,
    astonished int,
    e_mail varchar(256),
    primary key (e_mail),
    foreign key (id) references archives_mock(id)
);
insert into reactions_mock values
(
    1,
    1,
    1,
    0,
    0,
    "abc@email.com"
);
insert into reactions_mock values
(
    2,
    1,
    0,
    1,
    0,
    "def@email.com"
);
insert into reactions_mock values
(
    3,
    1,
    0,
    0,
    1,
    "ghi@email.com"
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