import time
import math

MAX_BUCKET_SIZE = 3
REFILL_RATE = 1 

class TokenBucket:
    def __init__(self):
        self.current_bucket_size = MAX_BUCKET_SIZE
        self.last_refill_timestamp = time.time()

    def allow_request(self, tokens):
        self.refill()  

        if self.current_bucket_size >= tokens:
            self.current_bucket_size -= tokens
            return True
        return False

    def refill(self):
        now_time = time.time()
        elapsed_time = now_time - self.last_refill_timestamp
        print(f"Elapsed time: {elapsed_time}")
        tokens_to_add = elapsed_time * REFILL_RATE

        self.current_bucket_size = min(self.current_bucket_size + tokens_to_add, MAX_BUCKET_SIZE)
        print(self.current_bucket_size)
        self.last_refill_timestamp = now_time

def main():
    bucket = TokenBucket()

    # Simulate requests
    print(f"Request processed: {bucket.allow_request(1)}") 
    print(f"Request processed: {bucket.allow_request(1)}") 
    print(f"Request processed: {bucket.allow_request(1)}")  
    print(f"Request processed: {bucket.allow_request(1)}")  

    time.sleep(2)

    print(f"Request processed: {bucket.allow_request(1)}")  

if __name__ == "__main__":
    main()
