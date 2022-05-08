--created schema- 'input'
create schema input

--created schema- 'output'
create schema output

create table input.sample1
(id int,
name varchar(20),
address varchar(20),
created_date date);

insert into input.sample1
values(1,'jugal','xyz street','2021-09-27'),
(2,'amit','abc street','2021-09-28');

insert into input.sample2
values(1,'sameer','rajasthan','2021-09-28'),
(2,'samrita','gujarat','2021-09-29');

select * from input.sample1;		select * from input.sample2

delete from output.sample1;		delete from output.sample2;

--schema- output
select * from output.sample1 
select * from output.sample2

--Rest Api:
select * from Rest




