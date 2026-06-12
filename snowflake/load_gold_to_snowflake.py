import pandas as pd
import snowflake.connector

conn = snowflake.connector.connect(
    user="GINGERGARLIC1899",
    password="Garlicginger@1899",
    account="WAVCZBP-JT57407",
    warehouse="COMPUTE_WH",
    database="PAYMENT_ANALYTICS",
    schema="RAW",
    role="ACCOUNTADMIN"
)

cursor = conn.cursor()

# CITY REVENUE
city_df = pd.read_parquet(
    "spark/gold/city_revenue"
)

cursor.execute("TRUNCATE TABLE CITY_REVENUE")

for _, row in city_df.iterrows():
    cursor.execute(
        """
        INSERT INTO CITY_REVENUE
        VALUES (%s,%s)
        """,
        (row["city"], float(row["total_amount"]))
    )

# MERCHANT REVENUE
merchant_df = pd.read_parquet(
    "spark/gold/merchant_revenue"
)

cursor.execute("TRUNCATE TABLE MERCHANT_REVENUE")

for _, row in merchant_df.iterrows():
    cursor.execute(
        """
        INSERT INTO MERCHANT_REVENUE
        VALUES (%s,%s)
        """,
        (row["merchant"], float(row["total_amount"]))
    )

# STATUS COUNTS
status_df = pd.read_parquet(
    "spark/gold/status_counts"
)

cursor.execute("TRUNCATE TABLE STATUS_COUNTS")

for _, row in status_df.iterrows():
    cursor.execute(
        """
        INSERT INTO STATUS_COUNTS
        VALUES (%s,%s)
        """,
        (row["status"], int(row["transaction_count"]))
    )

conn.commit()

print("Data loaded successfully!")

cursor.close()
conn.close()