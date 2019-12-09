replace empty string with null
```python
def replace(_):
    return (
        F.when(F.col(_) == F.lit(''), None)
        .otherwise(F.col(_))
        .alias(_)
    )
```
+ imports
```python
import pyspark.sql.functions as F
```
+ data
```python
df = spark.createDataFrame(
    [
        ('a', 123),
        ('a', 123),
        ('b', 123),
    ],
    ['col1', 'col2']
)
```