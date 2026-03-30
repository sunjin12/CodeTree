n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    is_sorted = True
    for j in range(n-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            is_sorted = False
    if is_sorted == True:
        break

print(' '.join(list(map(str, arr))))
        