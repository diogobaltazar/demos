```python
# pyspark

```

# pandas

[doc](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html)
```python
# src ------------------------------------------------------------------
df = pd.DataFrame(data = {
    'a': [1, 2, 3]
    , 'b': ['A', 'B', 'C']
})

pd.to_json(orient="records")

# output ---------------------------------------------------------------
[{"a":1,"b":"A"},{"a":2,"b":"B"},{"a":3,"b":"C"}]
```

```sql
-- sql

```
