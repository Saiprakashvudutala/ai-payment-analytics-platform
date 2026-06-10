from faker import Faker
import random
import pandas as pd
from datetime import datetime

fake = Faker()

MERCHANTS = [
    "Amazon",
    "Flipkart",
    "Swiggy",
    "Zomato",
    "Myntra",
    "BigBasket",
    "IRCTC"
]

CITIES = [
    "Hyderabad",
    "Bangalore",
    "Mumbai",
    "Pune",
    "Chennai",
    "Delhi"
]

STATUS = [
    "SUCCESS",
    "FAILED",
    "PENDING"
]


def generate_transaction():

    return {
        "txn_id": f"TXN{random.randint(100000,999999)}",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "sender_id": f"USR{random.randint(1000,9999)}",
        "receiver_id": f"USR{random.randint(1000,9999)}",
        "amount": round(random.uniform(10, 50000), 2),
        "merchant": random.choice(MERCHANTS),
        "city": random.choice(CITIES),
        "status": random.choice(STATUS)
    }


if __name__ == "__main__":

    transactions = []

    for _ in range(1000):
        transactions.append(generate_transaction())

    df = pd.DataFrame(transactions)

    df.to_csv("transactions.csv", index=False)

    print("Generated 1000 transactions successfully!")
    print(df.head())