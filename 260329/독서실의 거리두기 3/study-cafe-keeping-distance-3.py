n = int(input())
pos = list(map(int, input()))

max_a, max_b = 0, 0
last_one = 0
max_len = 0
# 최대 거리 갱신
for i in range(1, n):
    if pos[i] == 1:
        if max_len < i - last_one:
            max_len = i - last_one
            max_a, max_b = last_one, i
        last_one = i 

# 최대 거리 자리의 가운데에 1 추가
pos[(max_b + max_a) // 2] = 1

min_a, min_b = 0, 0
last_one = 0
min_len = int(1e9)
# 최소 거리 계산
for i in range(1, n):
    if pos[i] == 1:
        if min_len > i - last_one:
            min_len = i - last_one
            min_a, min_b = last_one, i
        last_one = i 

print(min_len)
