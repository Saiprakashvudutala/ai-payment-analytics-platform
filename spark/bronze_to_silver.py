from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import *

spark = (
    SparkSession.builder
    .appName("BronzeToSilver")
    .master("local[*]")
    .getOrCreate()
)

schema = StructType([
    StructField("txn_id", StringType(), True),
    StructField("timestamp", StringType(), True),
    StructField("sender_id", StringType(), True),
    StructField("receiver_id", StringType(), True),
    StructField("amount", DoubleType(), True),
    StructField("merchant", StringType(), True),
    StructField("city", StringType(), True),
    StructField("status", StringType(), True)
])

bronze_df = spark.read.parquet(
    "spark/bronze/payment_events"
)

parsed_df = bronze_df.select(
    from_json(
        col("payment_json"),
        schema
    ).alias("data")
)

silver_df = parsed_df.select("data.*")

silver_df.show(10, truncate=False)

silver_df.write.mode("overwrite").parquet(
    "spark/silver/payment_events"
)

print("Silver Layer Created Successfully!")

spark.stop()