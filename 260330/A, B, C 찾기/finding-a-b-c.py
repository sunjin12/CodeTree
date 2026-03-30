arr = list(map(int, input().split()))
arr.sort()
a = b = c = 0

a = arr[0]
b = arr[1]
c = arr[-1] - a - b

print(f"{a} {b} {c}")

