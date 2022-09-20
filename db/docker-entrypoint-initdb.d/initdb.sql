use api;
create table archives
(
    id int auto_increment,
    body varchar(1024),
    label int,
    scale int,
    created_at timestamp,
    e_mail varchar(256),
    primary key (id)
);
create table posts
(
    id int,
    primary key (id),
    foreign key (id) references archives(id)
);
create table reactions
(
    id int,
    thumbsup int,
    heart int,
    smile int,
    astonished int,
    e_mail varchar(256),
    primary key (e_mail),
    foreign key (id) references archives(id)
);
create table trends
(
    id int,
    thumbsup int,
    heart int,
    smile int,
    astonished int,
    primary key (id),
    foreign key (id) references archives(id)
);