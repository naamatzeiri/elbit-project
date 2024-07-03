from confluent_kafka import Producer
import time

def acked(err, msg):
    if err is not None:
        print(f"Failed to deliver message: {err}")
    else:
        print(f"Message produced: {msg.value()}")

p = Producer({'bootstrap.servers': 'localhost:9092'})

for i in range(10):
    p.produce('ABC', key=str(i), value=f'Message {i}', callback=acked)
    p.poll(1)

p.flush()