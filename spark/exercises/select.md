```python
# pyspark
df.select(cols_list)
df.select(*cols_list)
```

```python
# src ------------------------------------------------------------------
df = pd.DataFrame(data = {
    'a': [1, 2, 3],
    'b': ['a', 'b', 'c']
})

# select cols
df[['a']]
d.a

# select rows
df.iloc[['0']]

# output ---------------------------------------------------------------
   a  b
0  1  a
1  2  b
2  3  c

   a
0  1
1  2
2  3

   a
0  1
1  2
2  3

   a  b
0  1  a
```

```sql
-- sql
select col1, col2
from tbl
```
