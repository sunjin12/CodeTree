import sys

# 재귀 깊이 제한 해제 (기본값이 1000이라 큰 격자에서 에러가 날 수 있음)
sys.setrecursionlimit(10**6)

# 입력 받기
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

# 방향 벡터 (상, 하, 좌, 우)
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def dfs(x, y):
    # 현재 위치 방문 처리
    visited[x][y] = True
    count = 1  # 현재 칸(집) 카운트
    
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        
        # 격자 안이고, 집이 있고(1), 아직 방문하지 않았다면
        if in_range(nx, ny) and grid[nx][ny] == 1 and not visited[nx][ny]:
            # 재귀적으로 방문하며 리턴된 인원수를 더함
            count += dfs(nx, ny)
            
    return count

# 마을 정보 탐색
village_counts = []

for i in range(n):
    for j in range(n):
        # 사람이 살고 방문하지 않은 곳을 찾으면 새로운 DFS 시작
        if grid[i][j] == 1 and not visited[i][j]:
            village_counts.append(dfs(i, j))

# 결과 출력
village_counts.sort()
print(len(village_counts))
for count in village_counts:
    print(count)