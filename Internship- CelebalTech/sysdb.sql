create table Movies
(sno int,
MovieTitle varchar(20),
Date date);

insert into Movies values
(1,'The Shawshank Redemp','2021-07-23'),
(2,'Baby Driver','2021-07-23'),
(3,'The Godfather','2021-07-24'),
(4,'Gone Girl','2021-07-24'),
(5,'Work It','2021-07-25'),
(6,'Go Goa Gone','2021-07-25');

select * from Movies

insert into Movies
values(7,'Tuesdays and fridays','2021-07-26'),
(8,'Black Widow','2021-07-26');

---------------------------------------backup of database
IF NOT EXISTS
(SELECT * FROM sys.credentials
WHERE credential_identity = 'backupdata')
CREATE CREDENTIAL backupdata WITH IDENTITY = 'storageadftask'
,SECRET = 'h+FuBg0QVyFzVwhCilRzYudjwZvePe2vcTCnQtD5whgrgtIVTh311IPkOFn8QLnXZqCnW9LDO0TTPmWc8e3tNw=='


BACKUP DATABASE master
TO URL = 'https://storageadftask.blob.core.windows.net/output/sqlBacpac/master_072021.bacpac'
WITH CREDENTIAL = 'backupdata'
,COMPRESSION
,STATS= 5;
GO

--------------------------q29
create table SourceDemo(
[ roll no] int,   
name varchar(50),
address varchar(20),
city varchar(20),
[ phone no] int)

insert into SourceDemo values(1,'jugal','xyx','raj',455),(2,'jeh','pqp','guj',699);

select * from SourceDemo;  select * from demo;

create table demo
(sourceTable varchar(20),
sinkTable varchar(20),
jsonMapping varchar(max));

insert into demo values('SourceDemo','SinkDemo','{"type": "TabularTranslator","mappings": [{"source": {"name": " roll no","type": "Int32","physicalType": "int"},"sink": {"name": "rollno","type": "Int32","physicalType": "int"}},{"source": {"name": "name","type": "String","physicalType": "varchar"},"sink": {"name": "name","type": "String","physicalType": "varchar"}},{"source": {"name": "address","type": "String","physicalType": "varchar"},"sink": {"name": "address","type": "String","physicalType": "varchar"}}],"typeConversion": true,"typeConversionSettings": {"allowDataTruncation": true,"treatBooleanAsNumber": false}}
')

insert into SourceDemo values(1,'jugal','rajasthan','xyz'),(2,'amit','gujarat','pqr');

--INDEXING:

CREATE TABLE stud
(id INT,
name VARCHAR(50) NOT NULL,
gender VARCHAR(50) NOT NULL,
age INT NOT NULL);

EXECUTE sp_helpindex stud

CREATE CLUSTERED INDEX indexStud
ON stud(age ASC)

CREATE NONCLUSTERED INDEX indexStud2
ON stud(id ASC)

select * from stud where age= 34 --seek age= ci

select id from stud where id=1	--seek id= nci, select * = scan, --select id, age- seek, select id, name- scan

INSERT INTO stud
VALUES(1, 'Sara', 'Female', 34),
(2, 'Jon', 'Male', 20),
(3, 'Mike', 'Male', 54),
(4, 'Ana', 'Female', 10),
(5, 'Nick', 'Female', 29)

--use-case on indexing.

create table DemoIndex
(date datetime,
name varchar(20),
age int)

insert into DemoIndex 
values('2021-10-04 1:00:00','amit',21),
('2021-10-04 2:00:00','ajay',22),
('2021-10-04 3:00:00','jugal',23),
('2021-10-04 4:00:00','sameer',24),
('2021-10-05 1:00:00','sam',21),
('2021-10-05 2:00:00','julie',23),
('2021-10-05 3:00:00','jon',25),
('2021-10-05 4:00:00','jeh',24),
('2021-10-06 1:00:00','sara',26),
('2021-10-06 2:00:00','mike',21),
('2021-10-06 3:00:00','nick',22),
('2021-10-06 4:00:00','ana',23),
('2021-10-07 1:00:00','sue',25),
('2021-10-07 2:00:00','max',26),
('2021-10-07 3:00:00','mona',24),
('2021-10-07 4:00:00','rahul',21)

CREATE CLUSTERED INDEX indexDemo
ON DemoIndex(date ASC)

select * from DemoIndex where date < '2021-10-05'

--DYNAMIC ALIASING:
create table DAlias
(id int,
name varchar(20),
amount int,
date date);

insert into DAlias 
values(1,'jugal',1000,'2021-10-01'),
(2,'amit',2000,'2021-10-02'),
(3,'max',3000,'2021-10-03'),
(4,'julie',4000,'2021-10-04'),
(1,'jugal',1000,'2021-11-01'),
(2,'amit',2000,'2021-11-02'),
(3,'max',3000,'2021-11-03'),
(4,'julie',4000,'2021-11-04'),
(1,'jugal',1000,'2021-12-01'),
(2,'amit',2000,'2021-12-02'),
(3,'max',3000,'2021-12-03'),
(4,'julie',4000,'2021-12-04')

select * from DAlias 

create table AliasDemo
(id int,
name varchar(20),
Oct_Amt int,
Nov_Amt int,
Dec_Amt int)

declare @tmp table(name varchar(30),id int)
insert into @tmp select distinct(name),id from DAlias	
declare @x int= (select count(distinct(name)) from DAlias)	
while @x > 0	
begin	
	declare @Oct int =(select amount from DAlias where id=@x and month(date)='10')	
	declare @Nov int =(select amount from DAlias where id=@x and month(date)='11')	
	declare @Dec int =(select amount from DAlias where id=@x and month(date)='12')	
	
	insert into AliasDemo
	select distinct(d.id), d.name, @Oct, @Nov, @Dec from DAlias d where id = @x  

	set @Oct ='';	set @Nov ='';	set @Dec ='';
	set @x =@x -1	
end	

select * from AliasDemo;	--delete from AliasDemo

create table e
(EmployeeId int,
Action varchar(20),
Created dateTime);

insert into e values
(1,'In','2019-04-01 12:00:00'),
(1	,'Out'	,'2019-04-01 15:00:00'),
(2,'In','2019-04-01 17:00:00'),
(2,'Out','2019-04-01 21:00:00')

select * from e		

declare @z int = (select Created from e where Action =  'Out') 
declare @y int = (select Created from e where Action = 'in')

declare @tbl table(emp int , hours int)

insert into @tbl 

select cast(select created from e where Action = 'in' and EmployeeId = 1 except select created from e where Action= 'out' and EmployeeId = 1 as float)

create table orderss
(id	int,
userId int,
totalcount int,
created_at dateTime);

insert into orderss
values(334,	540, 0,'3/6/2017 0:49'),
(341,156,6230,'3/6/2017 10:43'),
(614,1153,0,'3/12/2017 18:49'),
(621,1013,0,'3/13/2017 7:39');

select * from orderss

select *,dateadd(day,7,created_at) as 'week start day'  from orderss