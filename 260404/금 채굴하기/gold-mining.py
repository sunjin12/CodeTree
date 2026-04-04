from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def is_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 마름모 채굴
# 길이 k까지 bfs 진행
def rhombus(x, y, k):
    gold = 0
    q = deque()
    q.append((x, y, 0))
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True
    dis, djs = [0, 0, 1, -1], [-1, 1, 0, 0]

    while q:
        i, j, l = q.popleft()
        if grid[i][j] == 1:
            gold += 1

        for di, dj in zip(dis, djs):
            ni, nj = i + di, j + dj
            if is_range(ni, nj) and not visited[ni][nj] and l+1 <= k:
                visited[ni][nj] = True
                q.append((ni, nj, l+1))
    
    return gold
        


# k 0~n-1까지 돌며 모든 격자 체크
max_gold = 0
for k in range(2*n-1):
    for i in range(n):
        for j in range(n):
            gold = rhombus(i, j, k)
            # 손해보는지 체크
            if k**2 + (k+1)**2 <= gold * m:
                max_gold = max(max_gold, gold)

print(max_gold)

