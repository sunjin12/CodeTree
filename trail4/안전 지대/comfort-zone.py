import sys
# 파이썬의 기본 재귀 깊이 제한은 1000이므로, 격자 크기가 클 때 런타임 에러를 방지하기 위해 늘려줍니다.
sys.setrecursionlimit(10**5)

def input():
    return sys.stdin.readline().rstrip()

# 입력 받기
n, m = map(int, input().split())
grid = []
max_height = 0

for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)
    max_height = max(max_height, max(row))

# 상하좌우 방향 배열
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y, k):
    # 격자 범위를 벗어나거나, 이미 방문했거나, 높이가 k 이하라면 (물에 잠김) 갈 수 없음
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] <= k:
        return False
    return True

def dfs(x, y, k):
    # 현재 위치 방문 처리
    visited[x][y] = True
    
    # 상하좌우 탐색
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny, k):
            dfs(nx, ny, k)

# 정답을 저장할 변수 (최초 k=1, 안전 지대 수=0으로 초기화)
best_k = 1
max_zone_cnt = 0

# k를 1부터 격자 내 최고 높이까지 1씩 증가시키며 탐색
for k in range(1, max_height + 1):
    visited = [[False] * m for _ in range(n)]
    zone_cnt = 0
    
    for i in range(n):
        for j in range(m):
            # 방문하지 않았고, 물에 잠기지 않는 높이(> k)라면 새로운 안전지대 시작
            if not visited[i][j] and grid[i][j] > k:
                dfs(i, j, k)
                zone_cnt += 1
                
    # 안전 영역의 수가 '초과'할 때만 갱신 (수가 같을 때는 가장 작은 K를 유지해야 하므로 > 사용)
    if zone_cnt > max_zone_cnt:
        max_zone_cnt = zone_cnt
        best_k = k

# 결과 출력
print(best_k, max_zone_cnt)