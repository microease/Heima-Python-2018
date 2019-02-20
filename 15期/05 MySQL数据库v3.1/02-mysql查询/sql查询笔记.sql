--数据的准备
--创建数据库
	create database python_test charset=utf8;
--使用数据库
	use python_test;
--显示使用的当前数据是哪个
	select database();
--创建表
	create table into  

--查询
--查询所有的字段
	select * from students;
	select * from classes;
	select id,name from classes;
	select name as 姓名,age as 年龄 from students;
	select s.name,s.age from students as s;
--去重
	select distinct gender from students;

-- 条件查询
-- 比较运算符
-- >
	select * from students where age>18;
-- <
	select * from students where age<18;
-- >=
-- <=
-- =
-- !=
-- <>

-- 逻辑运算符
--and
	select * from students where age > 18 and age <30;
	select * from students where age > 18 and gender="女";
--or
	select * from students where age >18 or height >=180;

-- not
	select * from students where not age >= 18 and gender =2;
	select * from students where not (age >= 18 and gender =2);
--模糊查询
--like 
	--查询以小开始的名字
	select name from students where name like "小%";
	--查询含有小的名字
	select name from students where name like "%小%";
	--查询有2个字的名字
	select name from students where name like "__";
	--查询至少有2个字的名字
	select name from students where name like "__%"

--rlike
	select name from students where name rlike "^周.*";
 

--not in 
	select name,age from students where age not in(12,18,34);
--between and
	select name,age from students where age between 18 and 34;
--排序
-- order by 字段
-- asc从小到大排序 升序
-- desc从大到小排序 降序
--查询年龄在18到34岁之间的男性，按照年龄从小到大排序
	select * from students where(age between 18 and 34) and gender =1 order by age asc;

--聚合函数
--查询男性有多少人，女性有多少人
	select count(*) from students where gender=1;

--查询最大年龄
	select max(age) from students;

--查询所有人年龄的综合
	select sum(age) from students;
--查询平均年龄
	select avg(age) from students;
--分组
	select gender,count(*) from students group by gender;
--计算男性的人数
	select gender,count(*) from students where gender = 1 group by gender;
--分页

--限制查询个数
	select * from students where gender=1 limit 2;
--限制从哪到哪
	select * from students limit 0,5;

--连接查询
	select * from students inner join classes on students.cls_id=classes.id;

--按照要求显示姓名和班级
	











































































































































































