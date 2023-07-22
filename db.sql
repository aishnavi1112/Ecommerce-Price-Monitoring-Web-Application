create table user(
    user_id serial primary key,
    name varchar(256) not null ,
    password varchar(16) not null,
    mobile varchar(10) not null,
    email varchar(256) not null
);

create table prod(
    prod_id serial primary key,
    url varchar(1024) not null,
    site varchar(256) not null,
    img varchar(256) not null,
    title varchar(256) not null,
    initial_price float not null,
    desired_price float not null,
    email varchar(256) not null,
    new_price float default null,
);

create table website(
    website_id serial primary key,
    name varchar(256),
    url varchar(1024) not null

)

create table tracking(
    tracking_id serial primary key,
    user_id int references user,
    product_id int references prod
)

create table notification(
    notification_id serial primary key,
    user_id int references user,
    product_id int references prod
)