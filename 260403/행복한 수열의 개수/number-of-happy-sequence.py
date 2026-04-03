n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


# 행복한 수열인지 확인
def is_happy(arr):
    l = len(arr)
    suc = 1
    max_suc = 1
    prev = arr[0]
    for i in range(1, l):
        if arr[i] == prev:
            suc += 1
            max_suc = max(max_suc, suc)
        else:
            prev = arr[i]
            suc = 1
    return max_suc >= m

cnt = 0
# 수열 뽑아내기
for i in range(n):
    if is_happy(grid[i]):
        cnt += 1

for i in range(n):
    arr = []
    for j in range(n):
        arr.append(grid[j][i])
    if is_happy(arr):
        cnt += 1

print(cnt)




