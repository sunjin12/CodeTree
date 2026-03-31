n = int(input())
arr = list(map(int, input().split()))

def heapify(l, i):
    largest = i
    left = 2 * i
    right = 2 * i  + 1

    if left < l and arr[left] > arr[largest]:
        largest = left

    if right < l and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(l, largest)

def heapsort():
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
    
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(i, 0)

heapsort()

print(" ".join(list(map(str, arr))))
