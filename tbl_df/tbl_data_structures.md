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
TBL2
```
id  iq     name    age

```
filter out null
```python
df = df.filter(F.col('colname').isNotNull())
```
filter by value
```python
# value
df = df.filter(F.col('colname') == F.lit(value))
```
aggregate into array
```python
 
```
-----
merge
```sql
TODO
```
after join eliminate duplicate columns (spark)
```sql
# for equal names on both sources, use list naming ['c1'] instead of df1['c1'] == df1['c2']
```
get current date
```sql
--teradata
select top 1 current_date from TBL --no matter which tbl
```

list tbl column names and data types
```sql
-- teradata
select
	ColumnName,
	case
		when ColumnType is null then 'unavailable'
		when ColumnType lie 'C%' then 'String'
		when ColumnType like 'I%' then 'Integer'
		when ColumnType = 'F' then 'Float'
		else ColumnType
	end as ColumnType
from DBC.ColumnsV
where
	DatabaseName = 'DTST40_SSL_MDM_WRK'
	and TableName = 'TW_VAS_RKEMMOVE'
order by ColumnID;

-- pyspark
df.printSchema()
```

limit LIMIT rows of TBL
```sql
# pyspark
df.show(LIMIT)

-- teradata
select top N * from TBL

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
selecting NTH row of TBL1 | qualify | having
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
show tables
```sql
-- teradata
show tables [{from|in} DB] [like 'PATT']
```
partitioning/repartitiong
```python
#pyspark
val x = (1 to 10).toList
val numbersDf = x.toDF('number')
numbersDf.rdd.partitions.size # => 4
numbersDf.write.csv('/Users/powers/Desktop/spark_output/numbers') 
# Partition A: 1, 2
# Partition B: 3, 4, 5
# Partition C: 6, 7
# Partition D: 8, 9, 10
# coalesce: decrease
val numbersDf2 = numbersDf.coalesce(2)
numbersDf2.rdd.partitions.size # => 2
numbersDf2.write.csv('/Users/powers/Desktop/spark_output/numbers2')
# Partition A: 1, 2, 3, 4, 5
# Partition C: 6, 7, 8, 9, 10
# repartition
val homerDf = numbersDf.repartition(2)
homerDf.rdd.partitions.size # => 2
# Partition ABC: 1, 3, 5, 6, 8, 10
# Partition XYZ: 2, 4, 7, 9
val bartDf = numbersDf.repartition(6)
bartDf.rdd.partitions.size # => 6
# Partition 00000: 5, 7
# Partition 00001: 1
# Partition 00002: 2
# Partition 00003: 8
# Partition 00004: 3, 9
# Partition 00005: 4, 6, 10
```
optimize
```sql
-- databricks
optimize [DB.]TBL [where PRED]
  [zorder by (COL_1, COL_2, ...)]
```
[row_number() over](https://forgetcode.com/teradata/1779-row-number) | teradata
[rank() over](https://forgetcode.com/teradata/1797-difference-row-number-vs-rank-functions) | teradata
[qualify]()
qualifying with rank , aggregates data on rank (`qualify rank() over`) and gets a quantity (`over (<group-order-stat>) > 0`) of the ordered (`over (<group-stat> order by <col--order-list>)`) result set.
```sql
-- diogo was before barbara
select id, iq, name, age, rank(name) from TBL2
-- 4	2	nuno	134	1
-- 1	1	diogo	21	2
-- 3	1	diogo	34	2
-- 2	1	barbara	12	4




-- barbara was before diogo
-- nuno is RANK 4 because diogo took 2 positions, rank 3 is no longer available
select id, iq, name, age, rank(name asc) from TBL2
-- 2	1	barbara	12	1
-- 3	1	diogo	34	2
-- 1	1	diogo	21	2
-- 4	2	nuno	134	4




select id, iq, name, age, rank(name)
from DTST40_SSL_MDM_WRK.test_tbl
group by iq
-- 1	1	diogo	21	1
-- 3	1	diogo	34	1
-- 2	1	barbara	12	3
-- 4	2	nuno	134	1

select id, iq, name, age, rank(name)
from DTST40_SSL_MDM_WRK.test_tbl
qualify rank(name) = 1
-- 4	2	nuno	134	1

select id, iq, name, age, rank(name)
from DTST40_SSL_MDM_WRK.test_tbl
qualify rank(name) = 2
-- 1	1	diogo	21	2
-- 3	1	diogo	34	2

select id, iq, name, age, rank(name)
from DTST40_SSL_MDM_WRK.test_tbl
qualify rank(name asc) = 1
-- 2	1	barbara	12	4

select id, iq, name, age, rank(name asc)
from DTST40_SSL_MDM_WRK.test_tbl
qualify rank(name asc) = 1
-- 2	1	barbara	12	1

select id, iq, name, age, rank(iq)
from DTST40_SSL_MDM_WRK.test_tbl
qualify rank() over (   -- take the rank of the group by
	partition by iq 	-- group by iq
	order by id			-- order each group by id
) > 0;
-- 1	1	diogo	21	2
-- 2	1	barbara	12	2
-- 3	1	diogo	34	2
-- 4	2	nuno	134	1

select id, iq, name, age, rank(iq)
from DTST40_SSL_MDM_WRK.test_tbl
qualify rank() over (   -- take the rank of the group by
	partition by iq 	-- group by iq
	order by id			-- order each group by id
) = 1;
-- 1	1	diogo	21	2
-- 4	2	nuno	134	1

select id, iq, name, age, rank(iq)
from DTST40_SSL_MDM_WRK.test_tbl
qualify rank() over (   -- take the rank of the group by
	partition by iq 	-- group by iq
	order by name		-- order each group by id
) = 1;
-- 2	1	barbara	12	2
-- 4	2	nuno	134	1

select id, iq, name, age, rank(name)
from DTST40_SSL_MDM_WRK.test_tbl
qualify rank() over (
	partition by iq
	order by name
) = 1;

select id, iq, name, age, rank(name)
from DTST40_SSL_MDM_WRK.test_tbl
qualify rank() over (
	partition by name
	order by name
) = 1;
-- 2	1	barbara	12	4
-- 3	1	diogo	34	2
-- 1	1	diogo	21	2
-- 4	2	nuno	134	1


-- 3	23	gi	14	500
-- 5	43	ze	24	501
-- 2	232	ca	21	100
-- 4	22	ca	21	200
-- 1	11	b	11	1.000
select id, iq, name, age, assholeness, rank(name)
from DTST40_SSL_MDM_WRK.test_tbl
qualify rank() over (
	partition by
		name
	order by
		id asc,
		iq asc

	) = 1
;
-- 1	11	b	11	1.000	5
-- 2	232	ca	21	100		3
-- 3	23	gi	14	500		2
-- 5	43	ze	24	501		1







```
read/write file to/from dataframe
```python
# IMPORT
import pandas as pd
import pyspark.sql.types as T
import pyspark.sql.functions as F
from difflib import SequenceMatcher

# LOCAL
sc = spark.sparkContext
OK = 0

def col_name_match_score(src = '', dest = '', leng = 1):
    '''
    Get the similarity rank between src and dest.
    Similarity compares by index, character with character.
    Similarity approaches 1.0.
    '''
    return SequenceMatcher(None, src, dest).ratio() / leng
  
  
def compare_ds(src_path, dest_path):
  """

  EXAMPLE
  
  src_path = '/mnt/commbi_lob_inlanddailydrivr/shipment_delivery_time_raw.parquet'
  dest_path = '/mnt/commbi_lob_inlanddailydrivr/shipment_delivery_time_raw.parquet'

  compare_ds(src_path, dest_path)
  """
  is_file_path = lambda _: '/' in _
  src = (
    spark.read.format("parquet").load("dbfs:" + src_path) if is_file_path(src_path)
    else spark.sql('select * from ' + src_path)
  )
  dest = (
    spark.read.format("parquet").load("dbfs:" + dest_path) if is_file_path(src_path)
    else spark.sql('select * from ' + dest_path)
  )
  
  src_schema = src.schema
  dest_schema = dest.schema
  
  # verify col naming and data types
  schema_match_score = 0.0
  type_match_score = lambda src, dest, leng = 1: int(src == dest) / leng
  
  src_len = len(src_schema)
  if src_len == len(dest_schema):
    for i in range(src_len):
      schema_match_score += (
        col_name_match_score(src_schema[i].name, dest_schema[i].name, src_len)
        + type_match_score(src_schema[i].dataType, dest_schema[i].dataType, src_len)
      ) / 2
  
  
  return schema_match_score


df = (
  spark.read.format('csv').options(header='true', inferschema='true')
  .load('/path-to-file.csv')
)
df.write.csv('/path-to-file.csv', header = True, mode='overwrite')
```
mount blob
```python
dbutils.fs.mount(
  source = 'wasbs://' + BLOB_CONTAINER + '@' + STORAGE_ACC + '.blob.core.windows.net',
  mount_point = BLOB_CONTAINER_MNT_PATH,
  extra_configs = {
    'fs.azure.account.key.' + STORAGE_ACC + '.blob.core.windows.net': dbutils.secrets.get(
      scope = DATABRICKS_WSPACE_SCOPE,
      key = KEY_VAULT_KEY
    )
  }
)
```
read csv from blob to dataset
```python
df = (
  spark
  .read.format('csv')
  .options(header='true', inferschema='true', delimiter = ';')
  .load(BLOB_CONTAINER_MNT_PATH + INLAND_RES_PNL_DUMP_FILE)
)
```
read partitioned orc from datalake to dataset
```python
TODO
```
create dataframe
```python
# IMPORT
import pandas as pd
import pyspark.sql.types as T
import pyspark.sql.functions as F

# LOCAL
df_fields = [
  T.StructField('service', T.StringType(), True),
]
df_schema = T.StructType(df_fields)
df = spark.createDataFrame(spark.sparkContext.emptyRDD(), df_schema)
```
dbutils
```python
%fs ls 'dbfs:/mnt/datalake-prod/raw/'
dbutils.fs.ls('/mnt/datalake-prod/raw/')
dbutils.fs.rm(output_blob_folder, True)
```

map column from dict
```python
import pyspark.sql.functions as F
from itertools import chain

mapping = {'key1' : 'val1', }
mapping_expr = create_map([F.lit(x) for x in chain(*mapping.items())])
df.withColumn("dest_col", mapping_expr.getItem(F.col("orig_col")))
```
switch/case
```python
from pyspark.sql import functions as F
df.select(df.name, F.when(df.age > 4, 1).when(df.age < 3, -1).otherwise(0))
```


-----

By ``ages``, get the first 2 ``name`` of the employees with the highest ``id``
```
id  name    age
---------------
5	alexis	3
9	jordan	4
```
```sql
-- teradata
select *
from DTST40_SSL_MDM_WRK.test_tbl_diogo
qualify row_number() over ( -- select the row by number
		partition by age    -- group the tbl by age
		order by id desc    -- enforce order into the group
	) <= 2                  -- with the order enforced, take the first 2 of each group
order by id desc
;
```
get dataframe from db tbl
```python
spark.sql('select * from commbi_model_prod.shipment_master_shipment')
```

```python
spark.read.format("parquet").load("dbfs:/path/src")
nb = "/Users/admdpm021@crb.apmoller.net/idd/logic/raw/testing-notebook-run"
U = dbutils.notebook.run(nb, 60)
```

-----
create table
+ ``multiset``/``set``: allow/prohibit duplicates
```sql
drop table DTST40_SSL_MDM_WRK.test_tbl;
create multiset table  DTST40_SSL_MDM_WRK.test_tbl, fallback(
	id   		integer,
    iq	 		integer,
	name   		varchar(30),
    age   		integer,
	assholeness	integer
) unique primary index (id);
insert into DTST40_SSL_MDM_WRK.test_tbl(id, iq, name, age, assholeness) values (1, 11, 'b', 11, 1000);
insert into DTST40_SSL_MDM_WRK.test_tbl(id, iq, name, age, assholeness) values (2, 232, 'ca', 21, 100);
insert into DTST40_SSL_MDM_WRK.test_tbl(id, iq, name, age, assholeness) values (4, 22, 'ca', 21, 200);
insert into DTST40_SSL_MDM_WRK.test_tbl(id, iq, name, age, assholeness) values (3, 23, 'gi', 14, 500);
insert into DTST40_SSL_MDM_WRK.test_tbl(id, iq, name, age, assholeness) values (5, 43, 'ze', 24, 501);

select id, iq, name, age, assholeness, rank(name)
from DTST40_SSL_MDM_WRK.test_tbl
qualify rank() over (
	partition by
		name
	order by
		id asc,
		iq asc,
		
	) = 1
;


--5	43	ze	24	501	1
--3	23	gi	14	500	2
--2	232	ca	21	100	3
--4	22	ca	21	200	3
--1	11	b	11	1.000	5


df = spark.createDataFrame(
  [
    ('a', 'b', 1),
    ('a', 'b', 2),
    ('a', 'b', 3),
    ('c', 'b', 4),
    ('a', 'b', 5),
    ('c', 'b', 6),
    ('c', 'b', 7),
  ],
  ['colA', 'colB', 'colC']
)
w =  Window.partitionBy(df.colA).orderBy(df.colC.desc()) # defaults to ascendent
(
  df
  .withColumn('test', F.row_number().over(w).alias('test'))
  .filter(F.col('test') == F.lit(1))
  .select('colA','colB','colC')
  .show()
)

"""
+----+----+----+
|colA|colB|colC|
+----+----+----+
|   c|   b|   4|
|   a|   b|   1|
+----+----+----+
"""
```
cast
```python
df = df.select(F.col('col-name').cast(T.DoubleType()))
```
replace
```python
df.select(F.regexp_replace(F.col('col-name'), '\'', '').alias('col-name'))
```

```python
# DATA ########################################################
''' test table
['str_col', 'int_col']
('abc', 1)
('def1', 2)
('def1', 3)
('def1', 3)
+-------+-------+
|str_col|int_col|
+-------+-------+
|    abc|      1|
|   def1|      2|
|   def1|      3|
|   def1|      3|
+-------+-------+


test_2 table:

['int_col', 'dt_col', 'str_col']
(3, datetime.datetime(2019, 1, 1, 0, 0), 'non-matching')
(3, datetime.datetime(2019, 1, 1, 0, 0), 'def1')
(4, datetime.datetime(2020, 1, 1, 0, 0), 'kil')
+-------+-------------------+------------+
|int_col|             dt_col|     str_col|
+-------+-------------------+------------+
|      3|2019-01-01 00:00:00|non-matching|
|      3|2019-01-01 00:00:00|        def1|
|      4|2020-01-01 00:00:00|         kil|
+-------+-------------------+------------+
'''


# SELECT DISTINCT #############################################

stat = (
    'select distinct str_col '
    + 'from test '
    #+ 'where test.str_col ~ \'[0-9]\''
)

df_res = df.select('str_col').distinct()


# REGEX #######################################################

stat = (
    'select * '
    + 'from test '
    + 'where test.str_col ~ \'[0-9]\''
)
df_res = df.filter(df['str_col'].rlike('[0-9]'))


# LIMIT #######################################################

stat = (
    'select * '
    + 'from test '
    + 'limit 1'
)
df_res = df.limit(1)


# GROUPING AND AGGREGATING ####################################

# grouping is used to get information F about the group
# grouping must be followed by an aggregation F of the group
# group by A, agg F by A, show (A, F)
# showing other cols requires grouping them as well
# (how would I display the agg result with more cols?)

stat = (
    'select round(avg(int_col), 2) as avg '
    + 'from test '
)
df_res = df.agg({"int_col": "avg"})
df_res = df.agg(F.round(F.avg(df['int_col']), 2).alias('avg'))


stat = (
    'select round(avg(int_col), 2) as avg '
    + 'from test '
    + 'group by str_col'
)
df_res = (
    df
    .groupBy('str_col')
    .agg(F.round(F.avg(df['int_col']), 2).alias('avg'))
)


stat = (
    'select str_col '
    + 'from test '
    + 'group by str_col '
)
df_res = (
    df
    .groupBy('str_col')
    .agg(F.count(df['int_col']))# obliged to specify an agg f
    .select('str_col')
)


stat = (
    'select * '
    + 'from test '
    + 'group by str_col, int_col '
)
df_res = (
    df
    .groupBy('str_col', 'int_col')
    .agg(F.count(df['int_col'])) # obliged to specify an agg f
    .select('str_col', 'int_col')
)
''' result
['str_col', 'int_col'] [('def1', 3), ('abc', 1), ('def1', 2)]
+-------+-------+
|str_col|int_col|
+-------+-------+
|   def1|      2|
|    abc|      1|
|   def1|      3|
+-------+-------+
'''


stat = (
    'select max(int_col) '
    + 'from test '
)
df_res = df.agg({"int_col": "max"})

stat = (
    'select max(int_col) '
    + 'from test '
    + 'group by str_col'
)
df_res = df.groupBy('str_col').agg({"int_col": "max"})


stat = (
    'select max(int_col) as max_int '
    + 'from test '
    + 'group by str_col '
    + 'having max(int_col) < 3 ' # could not use max_int
)
df_res = (
    df
    .groupBy('str_col')
    .agg(F.max(df['int_col']).alias('max_int'))
    .filter(F.col('max_int') < 3) # could not use df['max_int']
)


# ORDER/SORT ################################################

stat = (
    'select * '
    + 'from test '
    + 'order by int_col'
)
df_res = df.sort(df['int_col'])


# CAST ######################################################

stat = (
    'select dt_col::date '
    + 'from test_2 '
)
df_res = (
    df
    .withColumn(
        'new_col'
        , F.date_format('dt_col', "yyyy-MM-dd")
    )
    .select('int_col', 'new_col') 
    .withColumnRenamed('new_col', 'dt_col')
)
''' result
['dt_col'] [(datetime.date(2019, 1, 1),)]
+-------+----------+
|int_col|    dt_col|
+-------+----------+
|      3|2019-01-01|
+-------+----------+
'''


# JOIN ######################################################


# A.B (on 1 column)
stat = (
    'select * '
    + 'from test as t '
    + 'join test_2 as t2 ' # defaults to inner join
    + 'on t.int_col = t2.int_col;'
)
df_res = (
    df
    .join(df_2, 'int_col') # defaults to inner join
)
''' result
['str_col', 'int_col', 'int_col', 'dt_col', 'str_col']
('def1', 3, 3, datetime.datetime(2019, 1, 1, 0, 0), 'def1')
('def1', 3, 3, datetime.datetime(2019, 1, 1, 0, 0), 'non-matching')
('def1', 3, 3, datetime.datetime(2019, 1, 1, 0, 0), 'def1')
('def1', 3, 3, datetime.datetime(2019, 1, 1, 0, 0), 'non-matching')
+-------+-------+-------------------+------------+
|int_col|str_col|             dt_col|     str_col|
+-------+-------+-------------------+------------+
|      3|   def1|2019-01-01 00:00:00|non-matching|
|      3|   def1|2019-01-01 00:00:00|        def1|
|      3|   def1|2019-01-01 00:00:00|non-matching|
|      3|   def1|2019-01-01 00:00:00|        def1|
+-------+-------+-------------------+------------+
'''


# A.B (on 2 columns)
stat = (
    'select * '
    + 'from test as t '
    + 'join test_2 as t2 '
    + 'on t.int_col = t2.int_col '
    + 'and t.str_col = t2.str_col'
)
df_res = (
    df
    .join(df_2, ['int_col', 'str_col'], how = 'inner')
)
''' result
['str_col', 'int_col', 'int_col', 'dt_col', 'str_col']
('def1', 3, 3, datetime.datetime(2019, 1, 1, 0, 0), 'def1')
('def1', 3, 3, datetime.datetime(2019, 1, 1, 0, 0), 'def1')
+-------+-------+-------------------+
|int_col|str_col|             dt_col|
+-------+-------+-------------------+
|      3|   def1|2019-01-01 00:00:00|
|      3|   def1|2019-01-01 00:00:00|
+-------+-------+-------------------+
'''


# A+A.B
stat = (
    'select * '
    + 'from test as t '
    + 'left join test_2 as t2 '
    + 'on t.int_col = t2.int_col;'
)
df_res = (
    df
    .join(df_2, 'int_col', 'left')
 )
''' result
['str_col', 'int_col', 'int_col', 'dt_col', 'str_col']
('abc', 1, None, None, None)
('def1', 2, None, None, None)
('def1', 3, 3, datetime.datetime(2019, 1, 21, 0, 0), 'def1')
('def1', 3, 3, datetime.datetime(2019, 1, 1, 0, 0), 'non-matching')
('def1', 3, 3, datetime.datetime(2019, 1, 21, 0, 0), 'def1')
('def1', 3, 3, datetime.datetime(2019, 1, 1, 0, 0), 'non-matching')
+-------+-------+-------------------+------------+
|int_col|str_col|             dt_col|     str_col|
+-------+-------+-------------------+------------+
|      1|    abc|               null|        null|
|      3|   def1|2019-01-01 00:00:00|non-matching|
|      3|   def1|2019-01-21 00:00:00|        def1|
|      3|   def1|2019-01-01 00:00:00|non-matching|
|      3|   def1|2019-01-21 00:00:00|        def1|
|      2|   def1|               null|        null|
+-------+-------+-------------------+------------+
'''


# A-B
stat = (
    'select * '
    + 'from test as t '
    + 'left join test_2 as t2 '
    + 'on t.int_col = t2.int_col '
    + 'where dt_col is null; # need not specify the tbl
)
df_res = (
    df
    .join(df_2, 'int_col', 'left')
    .filter(F.col('dt_col').isNull()) # col means whatever ds res col, UNLESS it's ambiguous
)
''' result
['str_col', 'int_col', 'int_col', 'dt_col', 'str_col']
('abc', 1, None, None, None)
('def1', 2, None, None, None)
+-------+-------+------+-------+
|int_col|str_col|dt_col|str_col|
+-------+-------+------+-------+
|      1|    abc|  null|   null|
|      2|   def1|  null|   null|
+-------+-------+------+-------+
'''


# B+A.B
stat = (
    'select * '
    + 'from test as t '
    + 'right join test_2 as t2 '
    + 'on t.int_col = t2.int_col;'
)
df_res = (
    df
    .join(df_2, 'int_col', 'right')
)
''' result
['str_col', 'int_col', 'int_col', 'dt_col', 'str_col']
('def1', 3, 3, datetime.datetime(2019, 1, 21, 0, 0), 'def1')
('def1', 3, 3, datetime.datetime(2019, 1, 1, 0, 0), 'non-matching')
('def1', 3, 3, datetime.datetime(2019, 1, 21, 0, 0), 'def1')
('def1', 3, 3, datetime.datetime(2019, 1, 1, 0, 0), 'non-matching')
(None, None, 4, datetime.datetime(2020, 1, 2, 0, 0), 'kil')
+-------+-------+-------------------+------------+
|int_col|str_col|             dt_col|     str_col|
+-------+-------+-------------------+------------+
|      3|   def1|2019-01-01 00:00:00|non-matching|
|      3|   def1|2019-01-01 00:00:00|non-matching|
|      3|   def1|2019-01-21 00:00:00|        def1|
|      3|   def1|2019-01-21 00:00:00|        def1|
|      4|   null|2020-01-02 00:00:00|         kil|
+-------+-------+-------------------+------------+
'''


# B-A
stat = (
    'select * '
    + 'from test as t '
    + 'right join test_2 as t2 '
    + 'on t.int_col = t2.int_col '
    + 'where str_col is null;'
)
df_res = (
    df
    .join(df_2, 'int_col', 'right')
    .filter(df['str_col'].isNul())
)
''' result
['str_col', 'int_col', 'int_col', 'dt_col', 'str_col']
(None, None, 4, datetime.datetime(2020, 1, 2, 0, 0), 'kil')
+-------+-------+-------------------+-------+
|int_col|str_col|             dt_col|str_col|
+-------+-------+-------------------+-------+
|      4|   null|2020-01-02 00:00:00|    kil|
+-------+-------+-------------------+-------+

'''


# A+B
stat = (
    'select * '
    + 'from test as t '
    + 'full join test_2 as t2 '
    + 'on t.int_col = t2.int_col;'
)
df_res = (
    df
    .join(df_2, 'int_col', 'full')
)
''' result
['str_col', 'int_col', 'int_col', 'dt_col', 'str_col']
('abc', 1, None, None, None)
('def1', 2, None, None, None)
('def1', 3, 3, datetime.datetime(2019, 1, 21, 0, 0), 'def1')
('def1', 3, 3, datetime.datetime(2019, 1, 1, 0, 0), 'non-matching')
('def1', 3, 3, datetime.datetime(2019, 1, 21, 0, 0), 'def1')
('def1', 3, 3, datetime.datetime(2019, 1, 1, 0, 0), 'non-matching')
(None, None, 4, datetime.datetime(2020, 1, 2, 0, 0), 'kil')
+-------+-------+-------------------+------------+
|int_col|str_col|             dt_col|     str_col|
+-------+-------+-------------------+------------+
|      1|    abc|               null|        null|
|      3|   def1|2019-01-01 00:00:00|non-matching|
|      3|   def1|2019-01-21 00:00:00|        def1|
|      3|   def1|2019-01-01 00:00:00|non-matching|
|      3|   def1|2019-01-21 00:00:00|        def1|
|      2|   def1|               null|        null|
|      4|   null|2020-01-02 00:00:00|         kil|
+-------+-------+-------------------+------------+
'''


# (A-B)+(B-A)
stat = (
    'select * '
    + 'from test as t '
    + 'full join test_2 as t2 '
    + 'on t.int_col = t2.int_col '
    + 'where str_col is null '
    + 'or dt_col is null;'   # mind the OR instead of AND
)
def_res = (
    df
    .join(df_2, 'int_col', 'full')
    .where(df['str_col'].isNull() | df['str_col'].isNull())
)
''' result
['str_col', 'int_col', 'int_col', 'dt_col', 'str_col']
('abc', 1, None, None, None)
('def1', 2, None, None, None)
(None, None, 4, datetime.datetime(2020, 1, 2, 0, 0), 'kil')
+-------+-------+-------------------+-------+
|int_col|str_col|             dt_col|str_col|
+-------+-------+-------------------+-------+
|      1|    abc|               null|   null|
|      2|   def1|               null|   null|
|      4|   null|2020-01-02 00:00:00|    kil|
+-------+-------+-------------------+-------+
'''


# UNION/INTERSECTION/DIFFERENCE ###############################
stat = (
    'select t.int_col, t.str_col '
    + 'from test as t '
    + 'union all ' # all == include duplicate rows
    'select t2.int_col, t2.str_col '
    + 'from test_2 as t2 '
)
df_res = (
    df.select('int_col', 'str_col')
    .union(df_2.select('int_col', 'str_col'))
)
''' result
['int_col', 'str_col']
(1, 'abc')
(2, 'def1')
(3, 'def1')
(3, 'def1')
(3, 'non-matching')
(3, 'def1')
(4, 'kil')
+-------+------------+
|int_col|     str_col|
+-------+------------+
|      1|         abc|
|      2|        def1|
|      3|        def1|
|      3|        def1|
|      3|non-matching|
|      3|        def1|
|      4|         kil|
+-------+------------+
'''


stat = (
    'select t.int_col, t.str_col '
    + 'from test as t '
    + 'union ' 
    'select t2.int_col, t2.str_col '
    + 'from test_2 as t2 '
)
df_res = (
    df.select('int_col', 'str_col')
    .union(df_2.select('int_col', 'str_col'))
    .distinct() # remove duplicate rows
)
''' result
['int_col', 'str_col']
(3, 'def1')
(4, 'kil')
(2, 'def1')
(1, 'abc')
(3, 'non-matching')
+-------+------------+
|int_col|     str_col|
+-------+------------+
|      3|        def1|
|      4|         kil|
|      1|         abc|
|      3|non-matching|
|      2|        def1|
+-------+------------+
'''

stat = (
    'select t.int_col, t.str_col '
    + 'from test as t '
    + 'intersect ' 
    'select t2.int_col, t2.str_col '
    + 'from test_2 as t2 '
)
df_res = (
    df.select('int_col', 'str_col')
    .intersect(df_2.select('int_col', 'str_col'))
)
'''result
['str_col', 'int_col']
('def1', 3)
+-------+-------+
|str_col|int_col|
+-------+-------+
|   def1|      3|
+-------+-------+
'''


stat = (
    'select t.int_col, t.str_col '
    + 'from test as t '
    + 'except ' 
    'select t2.int_col, t2.str_col '
    + 'from test_2 as t2 '
)
df_res = (
    df
    .join(df_2, ['int_col', 'str_col'], 'left')
    .filter(df_2['dt_col'].isNull()) # so the col that df doesn't have
    .select('str_col', 'int_col')
)
'''result
['str_col', 'int_col']
('abc', 1)
('def1', 2)
+-------+-------+
|str_col|int_col|
+-------+-------+
|   def1|      2|
|    abc|      1|
+-------+-------+
'''

# DATA TYPES ##################################################
timestamp = 'https://www.postgresql.org/docs/9.1/functions-datetime.html'


# EXERCISES ###################################################
stat = (
    'select '
    + 'extract(year from dt_col) as year'
    + ', sum(int_col) ' # aggregation funct
    + 'from test_2 '
    + 'group by year '
    + 'order by year desc' # alias col year is recognized
)
df_res = (
    df
    .select(
        'int_col' # explicit col used up ahead
        , F.year('dt_col').alias('year'))
    .groupBy('year')
    .agg(F.sum('int_col').alias('sum')) # aggregation funct
    .sort(F.col('year').desc()) # recon alias col == F.col(col)
)
''' result
['year', 'sum']
(2020.0, 4)
(2019.0, 6)
+----+---+
|year|sum|
+----+---+
|2020|  4|
|2019|  6|
+----+---+
'''


# CURRYING
stat = (
    'select * '
    + 'from test as t '
    + 'where t.int_col in ('
        + 'select extract(day from dt_col) as day '
        + 'from test_2 as t2'
    + ')'
)

# the function must return a pyspark.sql.functions.udf
# and take any type of args
def in_days(col_name, days_df):
    days = list(
        map(
            lambda _: _[col_name]
            , days_df.collect()
        )
    )
    
    # currying: returning a function 
    # taking as args the non-specified args
    # which must be of type pyspark.sql.column
    @F.udf(returnType=T.BooleanType())
    def in_days_curry(col_value):
        return col_value in days
    
    return in_days_curry
    
df_res = (
    df
    .filter(
        in_days('day', df_2.select(F.dayofmonth('dt_col').alias('day'))) # currying with:
        (df['int_col']) # int_col column
    )
)
'''result
['str_col', 'int_col']
('abc', 1)
('def1', 2)
+-------+-------+
|str_col|int_col|
+-------+-------+
|    abc|      1|
|   def1|      2|
+-------+-------+
'''


# get all df.str_col, search them in df_2.str_col, get sum S of df_2.int_col,
# filter df by int_col, searching for divisors of S
stat = (
    'with S as ('
        + 'select sum(t2.int_col) as S '
        + 'from test_2 as t2 '
        + 'where t2.str_col not in ('
            # all distinct test strings
            + 'select distinct t.str_col '
            + 'from test as t '
        + ')'
    + ') '
    + 'select * '
    + 'from test as t, S '
    + 'where ((S.S * 2) % t.int_col) = 0 ' # as to get all even and 1
)

def filt_str(df):
    # cols of df
    df_col_vals = list(map(lambda _: _.str_col, df.collect()))

    @F.udf(returnType = T.BooleanType())
    def filt_str_udf(str_col_val):        
        return str_col_val not in df_col_vals
    
    return filt_str_udf

def filt_by_divisers(dividend):
    @F.udf(returnType = T.BooleanType())
    def filt_by_divisers_udf(col_val):
        return dividend % col_val == 0
        
    return filt_by_divisers_udf


df_res = (
    df
    .filter(
        filt_by_divisers( # currying
            df_2
            .filter( # currying
                filt_str(df.select('str_col'))
                (df_2['str_col'])
            )
            .select(F.sum('int_col').alias('sum'))
            .head().sum * 2 # as to get all even and 1
        )
        (df['int_col'])
    )
)
'''result
['str_col', 'int_col', 's']
('abc', 1, 7)
('def1', 2, 7)
+-------+-------+
|str_col|int_col|
+-------+-------+
|    abc|      1|
|   def1|      2|
+-------+-------+
'''
```
