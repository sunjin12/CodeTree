N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]

# 초기값 설정
dp[0][0] = grid[0][0]

# 1. 첫 번째 열 채우기 (위에서 아래로만)
for r in range(1, N):
    dp[r][0] = dp[r-1][0] + grid[r][0]

# 2. 첫 번째 행 채우기 (왼쪽에서 오른쪽으로만)
for c in range(1, N):
    dp[0][c] = dp[0][c-1] + grid[0][c]

# 3. 나머지 칸 채우기 (질문하신 핵심 로직!)
for r in range(1, N):
    for c in range(1, N):
        dp[r][c] = max(dp[r-1][c], dp[r][c-1]) + grid[r][c]

max_num = 0
for row in dp:
    max_num = max(max_num, max(row))

print(max_num)