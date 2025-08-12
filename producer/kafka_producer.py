from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime

# Create Kafka producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Sample customers & products
customers = ['CUST001', 'CUST002', 'CUST003']
products = ['Laptop', 'Phone', 'Headphones', 'Keyboard']

while True:
    transaction = {
        "customer_id": random.choice(customers),
        "product": random.choice(products),
        "amount": round(random.uniform(100, 2000), 2),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    producer.send('transactions', value=transaction)
    print(f"Sent: {transaction}")
    time.sleep(2)  # send every 2 seconds
