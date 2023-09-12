from collections import Counter
import time

# Sample data with duplicates
data = [1, 2, 3, 4, 1, 2, 3, 4] * 10**7

# Using Counter
start_time = time.time()
counter = Counter(data)
end_time = time.time()
print("Using Counter:", end_time - start_time)

# Manual counting
start_time = time.time()
manual_counts = {}
for item in data:
    if item in manual_counts:
        manual_counts[item] += 1
    else:
        manual_counts[item] = 1
end_time = time.time()
print("Manual Counting:", end_time - start_time)
