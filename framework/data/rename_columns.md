

```python
# pyspark
df.select(
    F.col('col1').alias('COL1'),
    F.col('col2').alias('COL2')
)
```

```python
# pandas
df.rename(columns={
    "col1": "COL1",
    "col2": "COL2"
})
```

```sql
-- sql
select col1 as COL1, col2 as COL2
from tbl
```
