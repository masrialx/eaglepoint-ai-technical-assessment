import time
from collections import defaultdict

class RateLimiter:
    def __init__(self, max_requests=5, window_seconds=60):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.users = defaultdict(list)  # user_id -> list of timestamps

    def request(self, user_id):
        current_time = time.time()
        timestamps = self.users[user_id]

        # Remove expired timestamps
        self.users[user_id] = [t for t in timestamps if current_time - t < self.window_seconds]

        if len(self.users[user_id]) >= self.max_requests:
            return False  # request blocked
        else:
            self.users[user_id].append(current_time)
            return True  # request allowed

if __name__ == "__main__":
    limiter = RateLimiter()
    user = "user123"

    # Simulate 7 requests
    for i in range(7):
        allowed = limiter.request(user)
        print(f"Request {i+1}: {'Allowed' if allowed else 'Blocked'}")
        time.sleep(10)  # 10 seconds between requests
