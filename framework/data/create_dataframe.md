
```python
# pyspark

```

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
+ Primary pandas data structure
+ Two-dimensional, size-mutable, heterogeneous tabular data
+ Data structure contains labeled axes (rows and columns)
+ dict-like container for Series objects
+ can't declare data type per column, only overall
```python
# src ------------------------------------------------------------------
df = pd.DataFrame(data = {
    'a': [1, 2, 3],
    'b': ['abc', 'def', 'ghi']
})

# output ---------------------------------------------------------------
   a  b
0  1  a
1  2  b
2  3  c
```

```python
# src ------------------------------------------------------------------
df = pd.DataFrame(
    data = {
        'a': [1, 2, 3],
        'b': ['a', 'b', 'c']
    },
    index = [_ + 1 for _ in range(3)]
)

# output ---------------------------------------------------------------
   a  b
1  1  a
2  2  b
3  3  c
```

```python
# src ------------------------------------------------------------------
idx = pd.Index([_ + 1 for _ in range(3)], name='index')
df = pd.DataFrame(
    data = {
        'a': [1, 2, 3],
        'b': ['a', 'b', 'c']
    },
    index = idx
)

# output ---------------------------------------------------------------
       a  b
index
1      1  a
2      2  b
3      3  c
```

```python
# src ------------------------------------------------------------------
df = pd.DataFrame(
    data = np.array([
        [1, 'a'],
        [2, 'b'],
        [3, 'c'],
    ])
    , columns = ['a', 'b']
)
df.set_index('a', inplace = True)

# output ---------------------------------------------------------------
   b
a
1  a
2  b
3  c
```

```python
# src ------------------------------------------------------------------
df.axes
df.index

df.rename_axis('headers')

df.rename_axis('index', axis='columns')

df.rename_axis('index', axis='columns').rename_axis('headers')

df.rename_axis('index', axis='columns').rename_axis('headers').axes

# output ---------------------------------------------------------------
[Int64Index([1, 2, 3], dtype='int64'), Index(['a', 'b'], dtype='object')]
Int64Index([1, 2, 3], dtype='int64')

         a  b
headers
0        1  a
1        2  b
2        3  c

index  a  b
0      1  a
1      2  b
2      3  c

index    a  b
headers
0        1  a
1        2  b
2        3  c

[RangeIndex(start=0, stop=3, step=1, name='headers')
, Index(['a', 'b'], dtype='object', name='index')]
```

```sql
--sql

```
