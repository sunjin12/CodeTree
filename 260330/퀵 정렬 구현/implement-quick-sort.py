n = int(input())
arr = list(map(int, input().split()))

def quick_sort(start, end):
    if start >= end:
        return
    
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and arr[left] < arr[pivot]:
            left += 1

        while right > start and arr[right] > arr[pivot]:
            right -= 1
    
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            arr[right], arr[pivot] = arr[pivot], arr[right]
    
    quick_sort(left, right - 1)
    quick_sort(right + 1, end)

quick_sort(0, n-1)

print(" ".join(list(map(str, arr))))

