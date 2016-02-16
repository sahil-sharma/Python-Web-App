drop table if exists account_holder;
create table account_holder (
id integer primary key autoincrement,
username text not null,
password text not null,
homefolder text not null,
grantsudo numeric,
shelltype numeric
);

