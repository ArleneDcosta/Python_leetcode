import queue
import time
import threading
# Define a function that will process items from the queue
def process_queue(q,thread_no):
    while True:
        item = q.get()
        print(f'Processing item {item}...with thread_no {thread_no}\n')
        time.sleep(1)
        q.task_done()
# Create a queue and start the worker threads
if __name__ == '__main__':
    q = queue.Queue()
    for i in range(2):
        t = threading.Thread(target=process_queue, args=(q,i))
        t.daemon = True
        t.start()
    # Add some items to the queue
    for i in range(10):
        q.put(i)
    # Wait for the queue to be processed
    q.join()
    print('All items processed')