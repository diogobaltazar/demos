fields = [
    T.StructField('field1', T.StringType(), True),
    T.StructField('field2', T.IntegerType(), True),
    T.StructField('field3', T.StringType(), True),
]
schema = T.StructType(fields)
df = spark.createDataFrame(spark.sparkContext.emptyRDD(), schema)