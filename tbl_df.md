# tables and dataframes
TBL1
```
id  name    age
---------------
1	diogo	2
2	joão	2
3	lin	3
4	jonas	3
5	alexis	3
6	olivier	4
7	romaric	4
8	mikael	4
9	jordan	4
```

-----

limit LIMIT rows of TBL
```sql
# pyspark
df.show(LIMIT)

-- teradata
select * from TBL sample LIMIT

-- hiveql, oracle
select * from TBL limit LIMIT
```
show view V_TBL
```sql
-- teradata
show view V_TBL
```
select view V_TBL
```sql
select * from V_TBL
```
create tbl DB.TBL [teradata](https://docs.teradata.com/reader/wada1XMYPkZVTqPKz2CNaw/QgKhDvW0hFGCG0eElpW9TQ)
```sql
-- teradata
create multiset table  DB.TBL, fallback(
	id   integer,
    name   varchar(30),
    age   integer
) unique primary index (id);
```
insert into [teradata](https://teradata.github.io/presto/docs/0.167-t/sql/insert.html)
```sql
-- teradata
insert into DTST40_SSL_MDM_WRK.test_tbl_diogo (id, name, age)
values (1, 'b', 2);
```
selecting NTH row of TBL1
```sql
--teradata
select
	age,
	count(name)
from DTST40_SSL_MDM_WRK.test_tbl_diogo
group by age
qualify row_number() over (
		order by count(name) asc
	) = 1
;
```

-----
# exercises

By ``ages``, get the ``name`` of the emp with the highest ``id``
```sql
-- teradata
select *
from DTST40_SSL_MDM_WRK.test_tbl_diogo
qualify row_number() over ( -- select the row by number
		partition by age    -- group the tbl by age
		order by id desc    -- enforce order into the tbl
	) = 1                   -- with the order enforced, take the first
order by id desc
```
