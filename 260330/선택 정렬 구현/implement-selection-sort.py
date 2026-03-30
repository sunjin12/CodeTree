n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    min = i
    for j in range(i, n):
        if arr[min] > arr[j]:
            min = j
    
    arr[i], arr[min] = arr[min], arr[i]

print(' '.join(list(map(str, arr))))
        
