# Task 3 – Rate Limiter Documentation

## Searches & Resources:
- Google: "python rate limiter per user"
- Python defaultdict docs: https://docs.python.org/3/library/collections.html#collections.defaultdict
- Time handling: https://docs.python.org/3/library/time.html

## Thought Process:
- Use a dictionary to track each user's request timestamps
- Remove expired timestamps older than 60 seconds
- Block request if the user exceeded 5 requests in the window
- Simple class design to reuse logic

## Step-by-Step Process:
1. Initialize RateLimiter class
2. For each user, store timestamps of requests
3. Remove timestamps older than 60 seconds
4. Check if remaining timestamps < max_requests
5. Allow or block request
6. Test with multiple requests for same user

## Problems & Fixes:
- Initially forgot to clean old timestamps → fixed by filtering
- Tested edge case of exactly 5 requests

## Why this solution is optimal:
- Efficient O(1) insert per request
- Handles multiple users independently
- Auto-reset after window
- Easy to extend for larger applications
