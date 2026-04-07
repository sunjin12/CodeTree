from collections import deque

arr = deque(list(input()))
n = len(arr)

# Run-length Encoding
def rle(arr):
    output = []
    l = len(arr)
    consec = 1
    for i in range(1, n):
        if arr[i] == arr[i-1]:
            consec += 1
        else:
            output.append(arr[i-1])
            output.append(consec)
            consec = 1
    
    output.append(arr[l-1])
    output.append(consec)

    return len("".join(map(str, output)))

min_len = int(1e9)
# 0~n-1 쉬프트
for _ in range(n):
    min_len = min(min_len, rle(arr))
    arr.appendleft(arr.pop())

# 최소 길이 출력
print(min_len)