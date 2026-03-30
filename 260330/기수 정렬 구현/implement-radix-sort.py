n = int(input())
arr = list(map(int, input().split()))

MAX_DIGITS = 6
for i in range(MAX_DIGITS + 1):
    buckets = [[] for _ in range(10)]

    for j in range(n):
        digit = (arr[j] // (10**i)) % 10
        buckets[digit].append(arr[j])
    
    arr = [num for bucket in buckets for num in bucket]

for c in arr:
    print(c, end=' ')