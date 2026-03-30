n = int(input())
arr = list(map(int, input().split()))

def merge_sort(low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(low, mid)
        merge_sort(mid+1, high)
        merge(low, mid, high)

def merge(low, mid, high):
    global arr
    merged_list = [0] * (high - low + 1)
    # 두 리스트를 비교하며 작은 쪽을 합쳐진 리스트에 넣기
    i, j, k = low, mid + 1, 0
    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            merged_list[k] = arr[i]
            i += 1
            k += 1
        else:
            merged_list[k] = arr[j]
            j += 1
            k += 1

    # 남은 리스트 비우기
    while i <= mid:
        merged_list[k] = arr[i]
        i += 1
        k += 1

    while j <= high:
        merged_list[k] = arr[j]
        j += 1
        k += 1

    arr[low:high+1] = merged_list

merge_sort(0, n-1)

print(' '.join(list(map(str, arr))))
