/* CREATE 2 TABLES: tb1 AND tb2:
create table tb1
(id integer primary key,
name varchar(25) ,
address varchar(25));

create table tb2
(id integer foreign key references tb1(id),
name varchar(25) ,
age integer );

INSERTION OF VALUES IN BTH THE TABLE:

insert into tb1
values(1,'jugal','31-cross street'),
(2,'amit','jp road'),
(3,'anu','b32 colony'),
(4,'janvi','18-o street'),
(5,'sonu','21-howard street');

insert into tb2
values(1,'jugal',18),
(3,'anu',25),
(2,'amit',20);

select * from tb2;
select * from tb1;
*/

		--LEVEL:A
--update command
update tb1 set name='sanjay' where name='sonu'; 
select * from tb1;

--delete command
delete from tb1 where name= 'janvi';
select * from tb1;

--select top with like operator
select top 3 * from tb1 where name like 'A%';

--aggregate min,max
select min(age) as'Min-age', max(age) as 'Max-age' from tb2;

--aggregate count
select count(name) from tb1;

--aggregate avg
select avg(age) from tb2;

--aggregate sum
select sum(age) from tb2;

--in operator
select age from tb2 where age in (15,16,17,18,19,20);

--between operator
select age from tb2 where age between 10 and 30;

--inner join
select * from tb1 as t1 inner join tb2 as t2 on t1.id = t2.id;

--left join
select * from tb1 left join tb2 on tb1.id=tb2.id;

--right join
select * from tb1 right join tb2 on tb1.id=tb2.id;

--full join
select * from tb1 full join tb2 on tb1.id=tb2.id;

--self join
select * from tb1, tb2  where tb1.id<>tb2.id; 

--union
select id,name from tb1 
union 
select id,name from tb2;

--intersect
select id,name from tb1 
intersect 
select id,name from tb2;

--having and group by
select id, sum(age) from tb2 group by id having sum(age)<=60;

 --order by
select * from tb1 order by name desc;

--exsist
select * from tb1 where exists (Select * from tb2 where tb1.id=tb2.id and name like 'J%');

--any,all
select name from tb1 where name = any (select name from tb2 where age =20);

select name from tb1 where name= all(select name from tb2 where age in (18,20));

--case
select name,age, case
	when age<20 then 'age is less than 20'
	when age=20 then 'age is equal to 20'
	else 'age is more than 20'
end as 'message'
from tb2;

--stord procedure
create procedure x as
select * from tb1 
go;

exec x;

		--LEVEL:B

--create db
create database q1;

--backup db
backup database q1
to disk "/c:/desktop";

--view
create view [18+] as
select * from tb2 where age >=18;

select * from [18+];