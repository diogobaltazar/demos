```python
# pandas

df = pd.DataFrame(data = {
    'a': [1, 2, 3, 4],
    'b': ['Raw value', 'raw value', 'raw Value', 'Raw Value']
})
df[df.parameter_type.str.match(r'(R|r)aw (V|v)alue') == False]
```

```python
# spark

ds = spark.createDataFrame(
  [
    ('abc asd', 123),
    ('abc abd', 123),
    ('def', 123),
  ]
  , ['abc', 'def']
)
ds.filter(F.col('abc').rlike('(abc abd)|(def)')).show()
regexp_replace('column name', 'replace this', 'with that')
```
