from pyspark.sql import SparkSession
from pyspark.sql.functions import count, sum

spark = (
    SparkSession.builder
    .appName("SilverToGold")
    .master("local[*]")
    .getOrCreate()
)

silver_df = spark.read.parquet(
    "spark/silver/payment_events"
)

# 1. Revenue by City
city_revenue = (
    silver_df.groupBy("city")
    .agg(sum("amount").alias("total_amount"))
)

city_revenue.write.mode("overwrite").parquet(
    "spark/gold/city_revenue"
)

# 2. Revenue by Merchant
merchant_revenue = (
    silver_df.groupBy("merchant")
    .agg(sum("amount").alias("total_amount"))
)

merchant_revenue.write.mode("overwrite").parquet(
    "spark/gold/merchant_revenue"
)

# 3. Transaction Status Counts
status_counts = (
    silver_df.groupBy("status")
    .agg(count("*").alias("transaction_count"))
)

status_counts.write.mode("overwrite").parquet(
    "spark/gold/status_counts"
)

print("Gold Layer Created Successfully!")

spark.stop()