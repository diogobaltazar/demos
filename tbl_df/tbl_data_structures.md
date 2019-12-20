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
  .options(header='true', inferschema='true')
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

```
