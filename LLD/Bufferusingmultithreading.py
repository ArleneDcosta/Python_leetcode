import threading
import queue
import time
import random

# Bounded buffer size
BUFFER_SIZE = 5
buffer = queue.Queue(maxsize=BUFFER_SIZE)

# Number of producers and consumers
NUM_PRODUCERS = 3
NUM_CONSUMERS = 2

# Simulate producing items
def producer(producer_id):
    while True:
        item = random.randint(1, 100)
        time.sleep(random.uniform(0.1, 0.5))  # simulate production time

        buffer.put(item)  # blocks if buffer is full
        print(f"Producer {producer_id} produced item {item} | Buffer size: {buffer.qsize()}")

# Simulate consuming items
def consumer(consumer_id):
    while True:
        time.sleep(random.uniform(0.2, 0.7))  # simulate consumption time

        item = buffer.get()  # blocks if buffer is empty
        print(f"Consumer {consumer_id} consumed item {item} | Buffer size: {buffer.qsize()}")
        buffer.task_done()

# Create and start producer threads
for i in range(NUM_PRODUCERS):
    t = threading.Thread(target=producer, args=(i+1,), daemon=True)
    t.start()

# Create and start consumer threads
for i in range(NUM_CONSUMERS):
    t = threading.Thread(target=consumer, args=(i+1,), daemon=True)
    t.start()

# Keep the main thread alive to allow daemon threads to run

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Shutting down...")
