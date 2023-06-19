sudo -i -u postgres
psql postgres  (mak)
ALTER ROLE "asunotest" WITH LOGIN;


commands:
\du
\l
create user username with password 'password';
alter role username with superuser(or other);
create database name_database with owner name_owner;
\c change database

\d name_table

create table name_of_table(name varchar(50), last_name varchar(100), age int);
--------создает таблицу с полями (и типом данных)

drop table table_name
--------удаляет таблицу

insert into animal (name, last_name, age) values ('John', 'Snow', 20);
--------вводит название в поля

select * from animal
--------вытаскивает все значения из таблицы

serial primary key - задаем уникальную id

create table animal(
	id serial primary key, 
	name char(50) not null, 
	last_name text null, 
	age int check(age > 2), 
	middle_name varchar(50) default 'hello');

grant all privileges on database name_database to name_owner

create type gender as enum('M', 'W');

constraint name_check check (gender in ('M', 'W'))

select name as names from person;

select name || ' ' || age from person
select * from person limit 2;   первые 2
select distinct age from person;  -  уникальный возраст
select * from person where name (i не учитывает регистр)like 'J%';
select * from person where name like '_p%';
select * from person where age between 20 and 25;
select * from person order by age;   -    сортирует
asc - возрастание
desc - убывание
select count(*) from person -  показывает количество
select gender, count(*) from person group by gender  - количество по гендеру 
select name, case when age > 22 then 'no' else 'yes' end from person;
alter - меняет название
alter table person rename to person2;
alter table person2 add column last_name text;
alter table person2 rename column last_name to surname;
alter table person2 alter column surname type varchar(10);
alter table person2 drop column surname;
alger table person2 add constrain check_age check(age > 2);

avg - среднее арифметическое
select avg(age) from person2;

select gender, count(*) from person2 group by gender having count(*) > 2;

update
update person2 set name = 'john2' where id = 5;

delete
delete from person2 where id = 8
delete from person where age < 20;

nulls first
nulls last
select distinct on(name) name, age from person order by name, person desc;
...limit offset 3
fetch first(10) row only

foreign key (name_cat_id) references name_table(id) (on delete cascad)
select product.id, product.name, product.price, category.name from product join category on product.category_id = category.id;
select p.id, p.name, c.name from product as p join category as c on p.category_id = c.id;

create table passport(
id serial primary key,
pin int not null,
person_id int unique references person(id)
);

\copy (select * from student_teacher) to '/home/hello/Рабочий стол/h.txt' 

create index name_index  on name_table (name_column)
drop index name_index
select product.name from product union select category.name from category;

timestamp
select row(level) from name_table

Экспорт
pg_dump -U <username> -d 'dbname' > 'file.sql'

Импорт
psql <db_name> < <file_name>

