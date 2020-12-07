
```python
# src ------------------------------------------------------------------
df = pd.DataFrame(data = {
    'a': ['a', 'a', 'b', 'c']
    , 'b': ['A', 'B', 'B', 'C']
    , 'c': [1, 21, 2, 3]
    , 'd': [0, 0, 0, 0]
})

df = df.pivot(index=['a', 'd'], columns='b', values='c')

df.reset_index().rename_axis('', axis='columns')

# output ---------------------------------------------------------------
   a  b   c  d
0  a  A   1  0
1  a  B  21  0
2  b  B   2  0
3  c  C   3  0

b      A     B    C
a d
a 0  1.0  21.0  NaN
b 0  NaN   2.0  NaN
c 0  NaN   NaN  3.0

   a  d    A     B    C
0  a  0  1.0  21.0  NaN
1  b  0  NaN   2.0  NaN
2  c  0  NaN   NaN  3.0
```
