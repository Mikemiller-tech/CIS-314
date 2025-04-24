import random
import secrets
import time
from collections import Counter

# Generate 100 random numbers between 1 and 16 using random
random_numbers = [random.randint(1, 16) for _ in range(100)]

# Generate 100 random numbers between 1 and 16 using secrets
secrets_numbers = [secrets.randbelow(16) + 1 for _ in range(100)]

# Count unique numbers
random_counts = Counter(random_numbers)
secrets_counts = Counter(secrets_numbers)

print("\nCount of unique numbers (1-16):")
print("Random module:")
for num, count in sorted(random_counts.items()):
    print(f"  {num}: {count}")
print("Secrets module:")
for num, count in sorted(secrets_counts.items()):
    print(f"  {num}: {count}")

# Generate 100 random numbers between 1 and 65535 using random
random_large = [random.randint(1, 65535) for _ in range(100)]

# Generate 100 random numbers between 1 and 65535 using secrets
secrets_large = [secrets.randbelow(65535) + 1 for _ in range(100)]

# Count unique numbers
random_large_counts = Counter(random_large)
secrets_large_counts = Counter(secrets_large)

print("\nCount of unique numbers (1-65535):")
print("Random module:")
for num, count in sorted(random_large_counts.items()):
    print(f"  {num}: {count}")
print("Secrets module:")
for num, count in sorted(secrets_large_counts.items()):
    print(f"  {num}: {count}")

# Check for duplicates
print("\nDuplicate Check:")
print("Duplicates in random (1-65535):", any(count > 1 for count in random_large_counts.values()))
print("Duplicates in secrets (1-65535):", any(count > 1 for count in secrets_large_counts.values()))

# Sorting function (intentionally inefficient for longer time)
def custom_sort(arr):
    start_time = time.time()
    for i in range(len(arr)):
        for j in range(len(arr) - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]  # Bubble Sort (slow method)
    end_time = time.time()
    print(f"Custom sort time: {end_time - start_time:.6f} seconds")
    return arr

# Function to time the built-in sort with explicit loops
def timed_builtin_sort(arr):
    start_time = time.time()
    for _ in range(1):  # Ensuring time is measured within a loop
        arr.sort()
    end_time = time.time()
    print(f"Built-in sort time: {end_time - start_time:.6f} seconds")

# Generate and sort 100-element list (1-16)
sort_list = [random.randint(1, 16) for _ in range(100)]
print("\nSorting 100-element list (1-16):")
custom_sort(sort_list[:])  # Timing custom sort
timed_builtin_sort(sort_list[:])

# Generate and sort 100-element list (1-65535)
sort_large = [random.randint(1, 65535) for _ in range(100)]
print("\nSorting 100-element list (1-65535):")
custom_sort(sort_large[:])
timed_builtin_sort(sort_large[:])

# Generate and sort 500-element list (1-65535)
sort_larger = [random.randint(1, 65535) for _ in range(500)]
print("\nSorting 500-element list (1-65535):")
custom_sort(sort_larger[:])
timed_builtin_sort(sort_larger[:])
