from kafka import KafkaProducer
import json
import sys
import os
import time

# Add data-generator folder to path
sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "data-generator"
    )
)

from payment_event_generator import generate_transaction

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

TOPIC_NAME = "payments"

print("Producing payment events...")

while True:
    transaction = generate_transaction()

    producer.send(
        TOPIC_NAME,
        value=transaction
    )

    print(transaction)

    time.sleep(1)