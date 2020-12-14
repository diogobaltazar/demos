```python
# https://stackoverflow.com/questions/26716616/convert-a-pandas-dataframe-to-a-dictionary/26716774#26716774
# src ------------------------------------------------------------------
import pandas as pd
import functools as f

df = pd.DataFrame(data = {
    'a': [1, 2, 3],
    'b': ['a', 'b', 'c']
})

f.reduce(lambda x, y: {**x, **y}, [ {_[1]: _[2]} for _ in list(df.to_records()) ])

df.set_index('a').T.to_dict('list')

# output ---------------------------------------------------------------
   a  b
0  1  a
1  2  b
2  3  c

{1: 'a', 2: 'b', 3: 'c'}

{1: ['a'], 2: ['b'], 3: ['c']}
```
