import random
df = spark.createDataFrame(
    [
        (random.randint(1000, 9999), random.randint(1000, 9999))
    ],
    ['colA', 'colB']
)
