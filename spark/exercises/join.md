# pandas
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.join.html
something about setting indexes in pandas...

## TODO analyse
join with index
```python
# data
results = pd.read_csv(
    filepath_or_buffer='/home/dipm/tmp/data/clean/pre_pca.csv',
    sep = ',',
    delimiter = None,
    header = 'infer',
)[['method', 'parameter']]

# encodes
m = pd.read_csv(
    filepath_or_buffer='/home/dipm/tmp/data/utils/method_encode.csv',
    sep=',',
    delimiter=None,
    header='infer',
)
p = pd.read_csv(
    filepath_or_buffer='/home/dipm/tmp/data/utils/parameter_encode.csv',
    sep=',',
    delimiter=None,
    header='infer',
)

results = results.drop_duplicates(['method', 'parameter'])

results = (
    results
    .join(m.set_index('method'), on='method', lsuffix='_left', rsuffix='_right') # would not work without this because Im selecting the parameter col, otherwise it would be fine
    .join(p.set_index('parameter'), on='parameter', lsuffix='_left', rsuffix='_right')
)

results["pca_encoding"] = (
    results['method_encode']
    + '_' + results['parameter_encode']
)

results = results[['method', 'parameter', 'pca_encoding']]

print(results)
```

join with multiindex
```python
# src ------------------------------------------------------------------
df = pd.DataFrame(data = {
    'a': [1, 2, 3]
    , 'b': ['a', 'b', 'c']
    , 'c': ['A', 'B', 'C']
})

df.set_index(
    pd.MultiIndex.from_frame()
    , inplace=True
)

gf = pd.DataFrame(data = {
    'b': ['a', 'b', 'c']
    , 'c': ['A', 'B', 'C']
    , 'd': [11, 22, 33]
})


# output ---------------------------------------------------------------

```

```python
# src ------------------------------------------------------------------
df = pd.DataFrame(data = {
    'a': [1, 2, 3]
    , 'b': ['a', 'b', 'c']
    , 'c': ['A', 'B', 'C']
})

gf = pd.DataFrame(data = {
    'b': ['a', 'b', 'c']
    , 'c': ['A', 'B', 'C']
    , 'd': [11, 22, 33]
})

df.join(gf.set_index(['b', 'c']), on=['b', 'c'])

# output ---------------------------------------------------------------
   a  b  c   d
0  1  a  A  11
1  2  b  B  22
2  3  c  C  33

```
