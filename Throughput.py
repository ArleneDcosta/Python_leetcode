import time

class JobProcessor:
    def __init__(self):
        self.queue = []
        self.processed_jobs = 0

    def add_job(self):
        self.queue.append(time.time())

    def process_job(self):
        if self.queue:
            start_time = self.queue.pop(0)
            end_time = time.time()
            response_time = end_time - start_time
            latency = end_time - start_time
            self.processed_jobs += 1
            return response_time, latency
        else:
            return None, None

    def get_throughput(self, elapsed_time):
        return self.processed_jobs / elapsed_time

# Usage example
job_processor = JobProcessor()

# Simulate job arrivals
for _ in range(10):
    job_processor.add_job()
    time.sleep(0.1)

# Process jobs and measure response time and latency
while True:
    response_time, latency = job_processor.process_job()
    if response_time is None:
        break
    print(f"Response Time: {response_time:.3f}s, Latency: {latency:.3f}s")
    time.sleep(0.1)

elapsed_time = time.time()
throughput = job_processor.get_throughput(elapsed_time)
print(f"Throughput: {throughput:.2f} jobs/second")