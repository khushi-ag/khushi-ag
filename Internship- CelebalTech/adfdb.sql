
--created schema- 'input'
create schema input

create table input.sample1
(id int,
name varchar(20),
address varchar(20),
created_date date);

insert into input.sample1
values(1,'jugal','xyz street','2021-09-22'),
(2,'amit','abc street','2021-09-23');

insert into input.sample2
values(1,'sameer','rajasthan','2021-09-21'),
(2,'samrita','gujarat','2021-09-22');

select * from input.sample1;		select * from input.sample2

delete from output.sample1;		delete from output.sample2;

--schema- output
select * from output.sample1 
select * from output.sample2

select max(created_date) from output.sample1 

/*
task: Incremental Load without watermark

--create schema- 'output'; default schema-'dbo'
create schema output

create table lookup_table
(tablename varchar(20),
filename varchar(20),
folderpath varchar(20),
lastuptdt date,
date_col varchar(20))

insert into lookup_table values
('sample1','s1.csv','output/delta','1990-01-01','created_date'),
('sample2','s2.csv','output/delta','1990-01-01','created_date');

--schema- dbo
create table sample2
(id int,
name varchar(20),
address varchar(20),
created_date date)

delete from dbo.sample2

insert into sample1
values(1,'jugal','xyz street','2021-09-20'),
(2,'amit','abc street','2021-09-21');

insert into sample2
values(1,'sameer','rajasthan','2021-09-21'),
(2,'sonu','gujarat','2021-09-22');

create proc sp_updateMAxDate @date_col varchar(20), @table_Name varchar(20), @Schema_Name varchar(20) as exec
('update dbo.lookup_table 
set lastuptdt= (select max( ' + @date_Col+ ') from '+ @Schema_Name + '.' +@Table_Name + ')
where tablename = '''+@table_Name+ '''')

sp_helptext sp_updateMAxDate

--schema- output
create table output.sample2
(id int,
name varchar(20),
address varchar(20),
created_date date)

---------check:---------
--schema- dbo
select * from lookup_table
select * from sample1
select * from sample2

--schema- output
select * from output.sample1 
select * from output.sample2
---------check:---------

alter table lookup_table
add jsonmapping varchar(max) 

update lookup_table set jsonmapping= ' {"type": "TabularTranslator","mappings": [{"source": {"type": "String","ordinal": 1},"sink": {"name": "id","type": "Int32","physicalType": "int"}},{"source": {"type": "String","ordinal": 2},"sink": {"name": "name","type": "String","physicalType": "varchar"}},{"source": {"type": "String","ordinal": 3},"sink": {"name": "address","type": "String","physicalType": "varchar"}},{"source": {"type": "String","ordinal": 4},"sink": {"name": "created_date","type": "DateTime","physicalType": "date"}}],"typeConversion": true,"typeConversionSettings": {"allowDataTruncation": true,"treatBooleanAsNumber":false}}' 
where tablename= 'sample2'

--------------------------------------dynamic mapping
create table emp
(emp_id int,
emp_name varchar(20),
gender varchar(20),
dept_id int);

create table dept
(dept_id int,
dept_name varchar(20));

create table mapping
(sourcefilename varchar(20),
sinkschema varchar(20),
sinkname varchar(20),
jsonmapping varchar(max));

insert into mapping
values('emp.xlsx','dbo','emp',' {"type": "TabularTranslator","mappings": [{"source": {"name": "empid","type": "String","physicalType": "String"},"sink": {"name": "emp_id","type": "Int32","physicalType": "int"}},{"source": {"name": "empname","type": "String","physicalType": "String"},"sink": {"name": "emp_name","type": "String","physicalType": "varchar"}},{"source": {"name": "gender","type": "String","physicalType": "String"},"sink": {"name": "gender","type": "String","physicalType": "varchar"}},{"source": {"name": "deptid","type": "String","physicalType": "String"},"sink": {"name": "dept_id","type": "Int32","physicalType": "int"}}],"typeConversion": true,"typeConversionSettings": {"allowDataTruncation": true,"treatBooleanAsNumber": false}}
'),
('dept.xlsx','dbo','dept',' {"type": "TabularTranslator","mappings": [{"source": {"name": "deptid","type": "String","physicalType": "String" },"sink": {"name": "dept_id","type": "Int32","physicalType": "int"}},{"source": {"name": "deptname","type": "String","physicalType": "String"},"sink": {"name": "dept_name","type": "String","physicalType": "varchar"}}],"typeConversion": true,"typeConversionSettings": {"allowDataTruncation": true,"treatBooleanAsNumber":false}}');

delete from mapping;		select * from mapping

select * from dept;		select * from emp
-----------------------------------------------------------------
--sp:1
create or ALTER PROCEDURE proc1(
@sink varchar(20), @source varchar(20)
)as
begin
declare @temp table(SourceTable varchar(20), SinkTable varchar(20), sourceCount int, sinkCount int)
declare @c1 int;
select @c1= count(*) from @source  --error:define scalr table

declare @c2 int;
select @c2= count(*) from @sink

declare @sql varchar(max);
set @sql = 'insert into '+ @temp+ 'values('+@source+','+@sink+','+@c1+','+@c2+') 
select * from @temp'
execute @sql
end

----------------------------------------------------------------------------------------------------------------------------------------x
--sp:2 ..old sp
create proc proc1 @s1 varchar(max), @s2 varchar(max) as 
begin
	declare @c1 int; 
	declare @c2 int;
	declare @c3 int;
	declare @d varchar(20);

	declare @sourcetble table(name varchar(20));select * from @sourcetble
	declare @sinktble table(name varchar(20))
	insert into @sourcetble values(@s1);
	insert into @sinktble values(@s2);

	set @d = (select getdate());
	declare @temp table(Date date, SourceTable varchar(20), SinkTable varchar(20), sourceCount int, sinkCount int, countDiff int);
	select @c1= count(*) from @s1 --sourceCount
	select @c2= count(*) from @s2 --sinkCount
	select @c3= @c1-@c2; --countDiff

	insert into @temp values(@d,@s1,@s2,@c1,@c2,@c3);
	select * from @temp 
end
drop proc proc1

exec proc1 @s1= 't1',@s2= 't2'
------------------------------------------
--sp:3...success #1
create or alter proc proc1 
(@sourcetbl varchar(20), @sinktbl varchar(20)) as exec
('select getdate() as Date, count(*) as SourceCount from '+@sourcetbl+'
select count(*) as SinkCount from '+@sinktbl)

exec proc1 @sourcetbl ='t1', @sinktbl='t2'

-----
create or alter proc proc1 (@sourcetbl nvarchar(120), @sinktbl nvarchar(120)) 
as begin
declare @query nvarchar(max)
set @query= (N'declare @temp table(sourceCount int, sinkCount int, SourceTable varchar(20), SinkTable varchar(20))
declare @c1 int; 
declare @c2 int; 
select @c1= count(*) from '+@sourcetbl+
'select @c2= count(*) from '+@sinktbl+
'insert into @temp values(@c1,@c2'+@sourcetbl+','+@sinktbl+')'+
'select * from @temp')
exec sp_executesql @query
end
------------------------------------------------
--Sp: 4...success #2
drop table temp

create or alter proc sp1 (@source varchar(20), @sink varchar(20)) as begin
declare @d date= (select getdate())
--declare @c1 int --= (select count(*) from @source)

--select @c1=count(*) from tableDetails where Sourcetable= @source
insert into temp values(@d,@source,@sink)
end

exec sp1 @source='t1',@sink='t2'

select * from temp

---------------------------------------------
--sp:5..X
--date,sinktblname,sourcetblnmae,sourcecount,sinkcount

create or alter proc procname(@source nvarchar(128),@sink nvarchar(128))
AS BEGIN
	declare @temp nvarchar(max)	
	declare @sql nvarchar(max)

	set @sql = (N'insert into '+@temp+ 'values('+@source+','+@sink+'); select * from '+@temp)
	exec sp_executesql @sql;
END

exec procname @source='t1', @sink='t2'
select * from @temp

-------------------------------------------------q17
create table t4
(sno int,
name varchar(20));

select * from t1;	select * from t2;	
insert into t1 values(1,'AAA'),(2,'BBB');

insert into t3 values(1,'CCC'),(2,'DDD');
select * from t3;	select * from t4; 

create table tableDetails
(Sourcetable varchar(20), Sinktable varchar(20))

insert into tableDetails values('t1','t2'),('t3','t4')

select * from tableDetails;		select * from temp

create table temp
(Date date,
sourceCount int,
sinkCount int,
Sourcetble varchar(20),
Sinktble varchar(20));

drop table temp

-----------------------------------------------------------------
--FISCAL YEAR:
create table sourceFiscal
(name varchar(20),
SampleDate date);

create table sinkFiscal
(name varchar(20),
SampleDate date,
FiscalYear varchar(20))

insert into sourceFiscal values('jugal','2021-08-10'),('jeh','2021-01-16')
('arjun','2020-02-02'),('sameer','2021-08-11');

select * from sourceFiscal;		select * from sinkFiscal;	--01>03 t=2021; f=2020

delete from sourceFiscal
-----------------------------------------
--SCD-2:
create table tbl_emp
(surrkey int identity(1,1),
empid int,
empname varchar(20),
gender varchar(20),
country varchar(20),
isactive int);

select * from tbl_emp

insert into tbl_emp
values(1002,'amit','male','xyz',1);

-------------------------q29
create table SinkDemo(
rollno int,   
name varchar(50),
address varchar(20))

select * from SinkDemo;		select * from SourceDemo;	

create table SourceDemo(
[roll no] int,   
name varchar(50),
address varchar(20),
city varchar(20),
[phone no] int)

insert into SourceDemo values(1,'jugal','xyx','raj',455),(2,'jeh','pqp','guj',699);


---------------------------task::consideration.
create table AvailabilityStatus 
(category varchar(max),
date date,
days decimal(5,2),
target int,
actual decimal(5,2));

create table DMR_CBConsiderations
(Category varchar(20),
date date,
Condition_Montioring decimal(5,2),
Schedule_Maintanance decimal(5,2),
Critical_Function_Testing decimal(5,2));

create table DMR_CBEquipment
(Category varchar(20),
date date,
Equipment varchar(20),
DateOfUnavailability varchar(20),
NumberOfDays varchar(20),
Remarks varchar(max))

create table lookup_mapping
(tablename varchar(max),
category varchar(max),
target int,
jsonMapping varchar(max));

insert into lookup_mapping 
values('AvailabilityStatus','gas processing plant',97,'{"type": "TabularTranslator","mappings": [{"source": {"name": "Category","type": "String"},"sink": {"name": "category","type": "String","physicalType": "varchar"}},{"source": {"name": "Prop_0","type": "String","physicalType": "String"},"sink": {"name": "date","type": "DateTime","physicalType": "date"}},{"source": {"name": "Prop_38","type": "String","physicalType": "String"},"sink": {"name": "days","type": "Decimal","physicalType": "decimal","scale": 2,"precision": 5}},{"source": {"name": "Target","type": "String"},"sink": {"name": "target","type": "Int32","physicalType": "int"}},{"source": {"name": "Prop_39","type": "String","physicalType": "String"},"sink": {"name": "actual","type": "Decimal","physicalType": "decimal","scale": 2,"precision": 5}}],"typeConversion": true,"typeConversionSettings": {"allowDataTruncation": true,"treatBooleanAsNumber": false}}
'),
('AvailabilityStatus','overall Plant Availability',98,'{"type": "TabularTranslator","mappings": [{"source": {"name": "Category","type": "String"},"sink": {"name": "category","type": "String","physicalType": "varchar"}},{"source": {"name": "Prop_0","type": "String","physicalType": "String"},"sink": {"name": "date","type": "DateTime","physicalType": "date"} },{"source": {"name": "Prop_2","type": "String","physicalType": "String"},"sink": {"name": "days","type": "Decimal","physicalType": "decimal","scale": 2,"precision": 5}},{"source": {"name": "Target","type": "String"},"sink": {"name": "target","type": "Int32","physicalType": "int"}},{"source": {"name": "Prop_3","type": "String","physicalType": "String"},"sink": {"name": "actual","type": "Decimal","physicalType": "decimal","scale": 2,"precision": 5}}], "typeConversion": true,"typeConversionSettings": {"allowDataTruncation": true,"treatBooleanAsNumber": false}}
'),
('AvailabilityStatus','critical equipment availability',97,'{"type": "TabularTranslator","mappings": [{"source": {"name": "Category","type": "String"},"sink": {"name": "category","type": "String","physicalType": "varchar"}},{"source": {"name": "Prop_0","type": "String","physicalType": "String"},"sink": {"name": "date","type": "DateTime","physicalType": "date"}},{"source": {"name": "Prop_35","physicalType": "String"},"sink": {"name": "days","type": "Decimal","physicalType": "decimal","scale": 2,"precision": 5}},{"source": {"name": "Target","type": "String"},"sink": {"name": "target","type": "Int32","physicalType": "int"}},{"source": {"name": "Prop_36","physicalType": "String"},"sink": {"name": "actual","type": "Decimal","physicalType": "decimal","scale": 2,"precision": 5}}],"typeConversion": true,"typeConversionSettings": {"allowDataTruncation": true,"treatBooleanAsNumber": false}}
'),
('AvailabilityStatus','platforms',97,'{"type": "TabularTranslator","mappings": [{"source": {"name": "Category","type": "String"},"sink": {"name": "category","type": "String","physicalType": "varchar"}},{"source": {"name": "Prop_0","type": "String","physicalType": "String"},"sink": {"name": "date","type": "DateTime","physicalType": "date"}}, {"source": {"name": "Prop_106","physicalType": "String"},"sink": {"name": "days","type": "Decimal","physicalType": "decimal","scale": 2,"precision": 5}},{"source": {"name": "Target","type": "String"},"sink": {"name": "target","type": "Int32","physicalType": "int"}},{"source": { "name": "Prop_107","physicalType": "String"},"sink": {"name": "actual","type": "Decimal","physicalType": "decimal","scale": 2,"precision": 5}}],"typeConversion": true,"typeConversionSettings": {"allowDataTruncation": true,"treatBooleanAsNumber": false}}'),
('AvailabilityStatus','Crude Stabilization Units',97,'{"type": "TabularTranslator","mappings": [{"source": {"name": "Category","type": "String"},"sink": {"name": "category","type": "String","physicalType": "varchar"}},{"source": {"name": "Prop_0","type": "String","physicalType": "String"},"sink": { "name": "date","type": "DateTime","physicalType": "date"}},{"source": {"name": "Prop_41",  "physicalType": "String"},"sink": {"name": "days","type": "Decimal","physicalType": "decimal","scale": 2,"precision": 5}}, {"source": { "name": "Target","type": "String"},"sink": {"name": "target","type": "Int32","physicalType": "int"}},{"source": {"name": "Prop_42","physicalType": "String"},"sink": {"name": "actual","type": "Decimal","physicalType": "decimal","scale": 2,"precision": 5}}],"typeConversion": true,"typeConversionSettings": {"allowDataTruncation": true,"treatBooleanAsNumber": false}}
'),
('AvailabilityStatus','Crude Export',97,'{"type": "TabularTranslator","mappings": [ {"source": {"name": "Category","type": "String"},"sink": {"name": "category","type": "String","physicalType": "varchar"}},{"source": {"name": "Prop_0","type": "String","physicalType": "String"},"sink": {"name": "date","type": "DateTime","physicalType": "date"}},{"source": {"name": "Prop_44","physicalType": "String"},"sink": {"name": "days","type": "Decimal","physicalType": "decimal","scale": 2,"precision": 5}},{"source": {"name": "Target","type": "String"},"sink": {"name": "target","type": "Int32","physicalType": "int"}},{"source": {"name": "Prop_45","physicalType": "String"},"sink": {"name": "actual","type": "Decimal","physicalType": "decimal","scale": 2,"precision": 5} }],"typeConversion": true,"typeConversionSettings": {"allowDataTruncation": true, "treatBooleanAsNumber": false}}
'),
('AvailabilityStatus','Power Generation Units',97,'{"type": "TabularTranslator","mappings": [{"source": {"name": "Category","type": "String"},"sink": {"name": "category","type": "String","physicalType": "varchar"}},{"source": {"name": "Prop_0","type": "String","physicalType": "String"},"sink": {"name": "date","type": "DateTime","physicalType": "date"}},{"source": {"name": "Prop_72","physicalType": "String"}, "sink": {"name": "days","type": "Decimal","physicalType": "decimal","scale": 2,"precision": 5}},{"source": {"name": "Target","type": "String"},"sink": {"name": "target","type": "Int32","physicalType": "int"}},{"source": {"name": "Prop_78","physicalType": "String"},"sink": {"name": "actual","type": "Decimal","physicalType": "decimal","scale": 2,"precision": 5}}],"typeConversion": true,"typeConversionSettings": {"allowDataTruncation": true,"treatBooleanAsNumber": false}}
'),
('AvailabilityStatus','Utilities',97,'{"type": "TabularTranslator","mappings": [{"source": {"name": "Category","type": "String"},"sink": {"name": "category","type": "String","physicalType": "varchar"}},{"source": {"name": "Prop_0","type": "String","physicalType": "String" },"sink": {"name": "date","type": "DateTime","physicalType": "date"}},{"source": {"name": "Prop_77","physicalType": "String"},"sink": {"name": "days","type": "Decimal","physicalType": "decimal","scale": 2,"precision": 5}},{"source": { "name": "Target","type": "String"},"sink": {"name": "target","type": "Int32","physicalType": "int"}},{"source": {"name": "Prop_73","physicalType": "String"},"sink": {"name": "actual","type": "Decimal","physicalType": "decimal","scale": 2,"precision": 5}}],"typeConversion": true, "typeConversionSettings": {"allowDataTruncation": true,"treatBooleanAsNumber": false}}
'),
('DMR_CBConsiderations','DMR-CBconsiderations',null,'{"type": "TabularTranslator","mappings": [{"source": {"name": "Category","type": "String"},"sink": {"name": "Category","type": "String","physicalType": "varchar"}},{"source": {"name": "Prop_0","type": "String","physicalType": "String"},"sink": {"name": "date","type": "DateTime","physicalType": "date"} },{"source": {"name": "Prop_218", "type": "String","physicalType": "String"},"sink": {"name": "Condition_Montioring","type": "Decimal","physicalType": "decimal","scale": 2,"precision": 5}},{"source": {"name": "Prop_219","type": "String","physicalType": "String"},"sink": {"name": "Schedule_Maintanance","type": "Decimal","physicalType": "decimal","scale": 2,"precision": 5}},{"source": {"name": "Prop_220","type": "String","physicalType": "String"},"sink": {"name": "Critical_Function_Testing","type": "Decimal","physicalType": "decimal","scale": 2,"precision": 5} }],"typeConversion": true,"typeConversionSettings": {"allowDataTruncation": true,"treatBooleanAsNumber": false}}
'),
('DMR_CBEquipment','DMR-CBEquipment1',null,'{"type": "TabularTranslator","mappings": [{"source": {"name": "Category","type": "String"},"sink": {"name": "Category","type": "String","physicalType": "varchar"} },{"source": {"name": "Prop_0","type": "String","physicalType": "String"},"sink": {"name": "date","type": "DateTime","physicalType": "date"}},{"source": {"name": "Prop_221","type": "String", "physicalType": "String"},"sink": {"name": "Equipment","type": "Decimal","physicalType": "decimal","scale": 2,"precision": 5}},{"source": {"name": "Prop_222","type": "String","physicalType": "String"},"sink": {"name": "DateOfUnavailability","type": "Decimal","physicalType": "decimal","scale": 2,"precision": 5}},{"source": {"name": "Prop_223","type": "String","physicalType": "String"},"sink": {"name": "NumberOfDays","type": "Decimal","physicalType": "decimal","scale": 2,"precision": 5}},{"source": {"name": "Prop_224","type": "String","physicalType": "String"},"sink": {"name": "Remarks","type": "Decimal","physicalType": "decimal","scale": 2,"precision": 5}}],"typeConversion": true,"typeConversionSettings": { "allowDataTruncation": true,"treatBooleanAsNumber": false}}
'),
('DMR_CBEquipment','DMR-CBEquipment2',null,'{"type": "TabularTranslator","mappings": [{"source": {"name": "Category","type": "String"},"sink": {"name": "Category","type": "String","physicalType": "varchar" }},{"source": {"name": "Prop_0","type": "String","physicalType": "String"},"sink": {"name": "date","type": "DateTime","physicalType": "date"}},{"source": {"name": "Prop_225","type": "String","physicalType": "String"},"sink": {"name": "Equipment","type": "Decimal","physicalType": "decimal","scale": 2,"precision": 5} },{"source": {"name": "Prop_226","type": "String","physicalType": "String"},"sink": {"name": "DateOfUnavailability","type": "Decimal","physicalType": "decimal","scale": 2,"precision": 5}},{"source": {"name": "Prop_227","type": "String","physicalType": "String"},"sink": {"name": "NumberOfDays","type": "Decimal","physicalType": "decimal","scale": 2,"precision": 5}},{"source": {"name": "Prop_228","type": "String","physicalType": "String"},"sink": {"name": "Remarks","type": "Decimal","physicalType": "decimal","scale": 2,"precision": 5}}],"typeConversion": true,"typeConversionSettings": {"allowDataTruncation": true,"treatBooleanAsNumber": false}}
')

*/	
select * from AvailabilityStatus order by date;	-- select * from lookup_mapping

select * from DMR_CBConsiderations order by date;		 select * from DMR_CBEquipment order by date

delete from AvailabilityStatus 
delete from DMR_CBConsiderations;	delete from DMR_CBEquipment

--------sp: 
create or alter proc spproc (@tbl varchar(30), @year varchar(20)) as exec
( 'delete from '+@tbl+' Where date >= concat('+@year+',''-03-31'')')

sp_helptext spproc

/*
create or alter proc spproc
(@tbl varchar(30)) as exec
(' declare @year int
if(month(getdate()) > 03)
begin
	set @year= datepart(year,getdate())
end
else
begin
	set @year= Dateadd(year,-1,getdate())
end
delete from '+@tbl+' where convert(varchar(max),date) >= convert(varchar(max),concat(@year,-03-31))')

--sp:2
create or alter proc spproc  
(@tbl varchar(30)) as exec  
( 'if(month(getdate()) > 03)  
begin  
 delete from '+@tbl+' where date >= convert(varchar(max),datepart(year,getdate()))
end')
*/
