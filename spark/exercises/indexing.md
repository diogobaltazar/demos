[see](https://www.geeksforgeeks.org/indexing-and-selecting-data-with-pandas/)

```python
# pyspark

```

```python
# src ------------------------------------------------------------------
df = pd.DataFrame(data = {
    'a': [1, 2, 3],
    'b': ['a', 'b', 'c']
})

df.loc[[0]]

df.set_index('a', inplace = True)
df.loc[[1]]
# output ---------------------------------------------------------------
   a  b
0  1  a
1  2  b
2  3  c

   a  b
0  1  a

   b
a
1  a
```
multiindex
```python
# src ------------------------------------------------------------------
df = pd.DataFrame(data = {
    'a': [1, 2, 3]
    , 'b': ['a', 'b', 'c']
    , 'c': ['A', 'B', 'C']
})

index = pd.MultiIndex.from_frame(df[['a', 'b']])
df = df.drop(['a', 'b'], axis=1)
df.set_index(index, inplace=True)

# output ---------------------------------------------------------------
   a  b  c
0  1  a  A
1  2  b  B
2  3  c  C

     c
a b
1 a  A
2 b  B
3 c  C
```

```sql
-- sql

```
