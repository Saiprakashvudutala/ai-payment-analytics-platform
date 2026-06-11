from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("TestSpark")
    .master("local[*]")
    .getOrCreate()
)

data = [
    ("Sai", 100),
    ("Prakash", 200)
]

df = spark.createDataFrame(
    data,
    ["name", "amount"]
)

df.show()

spark.stop()