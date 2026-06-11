from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("KafkaToBronze")
    .master("local[*]")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

df = (
    spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "localhost:9092")
    .option("subscribe", "payments")
    .option("startingOffsets", "earliest")
    .load()
)

bronze_df = df.selectExpr(
    "CAST(value AS STRING) AS payment_json"
)

query = (
    bronze_df.writeStream
    .format("parquet")
    .option(
        "path",
        "spark/bronze/payment_events"
    )
    .option(
        "checkpointLocation",
        "spark/bronze/checkpoints"
    )
    .outputMode("append")
    .start()
)

query.awaitTermination()