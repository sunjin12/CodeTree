n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

max_cnt = 0
# 옆으로 일자
for i in range(n):
    for j in range(m-2):
        cnt = 0
        for k in range(3):
            cnt += grid[i][j+k]
        max_cnt = max(max_cnt, cnt)

# 아래로 일자
for i in range(n-2):
    for j in range(m):
        cnt = 0
        for k in range(3):
            cnt += grid[i+k][j]
        max_cnt = max(max_cnt, cnt)

# 기역 4 가지
for i in range(n-1):
    for j in range(m-1):
        cnt = 0
        for k in range(2):
            for l in range(2):
                cnt += grid[i+k][j+l]
        # print(f"cnt:{cnt}, i:{i}, j:{j}")     
        for k in range(2):
            for l in range(2):
                t_cnt = cnt - grid[i+k][j+l]
                # print(f"t_cnt:{t_cnt}, i:{i}, j:{j}, k:{k}, l:{l}")
                max_cnt = max(max_cnt, t_cnt)

print(max_cnt)
        
