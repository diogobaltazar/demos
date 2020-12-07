ds = spark.createDataFrame(
  [
    ('abc asd', 123),
    ('abc abd', 123),
    ('def', 123),
  ]
  , ['abc', 'def']
)
ds.filter(F.col('abc').rlike('(abc abd)|(def)')).show()