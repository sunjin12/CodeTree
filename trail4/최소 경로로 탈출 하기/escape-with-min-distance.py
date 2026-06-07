import sys
from collections import deque

# 빠른 입력을 위한 설정
input = sys.stdin.readline

# 1. 입력 받기
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 방문 여부 및 최단 거리를 기록할 배열 (-1로 초기화)
# -1은 아직 방문하지 못했음을 의미합니다.
step = [[-1] * m for _ in range(n)]

# 상, 하, 좌, 우 이동을 위한 방향 벡터
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
    """격자 범위를 벗어나는지 확인하는 함수"""
    return 0 <= x < n and 0 <= y < m

def bfs():
    # 2. BFS 준비 (큐 생성 및 시작점 방문 처리)
    q = deque()
    
    q.append((0, 0))
    step[0][0] = 0  # 시작 지점의 이동 거리는 0
    
    # 3. 큐가 빌 때까지 탐색 진행
    while q:
        x, y = q.popleft()
        
        # 현재 위치에서 4방향으로 이동 시도
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            # 격자 내에 있고, 뱀이 없으며(1), 아직 방문하지 않은 칸(-1)인 경우
            if in_range(nx, ny) and grid[nx][ny] == 1 and step[nx][ny] == -1:
                step[nx][ny] = step[x][y] + 1  # 이전 칸의 거리 + 1
                q.append((nx, ny))

# BFS 탐색 시작
bfs()

# 4. 결과 출력 (도착점의 최단 거리 값을 출력)
# 탐색이 끝났는데도 -1이라면 도달할 수 없는 경로이므로 -1이 그대로 출력됩니다.
print(step[n-1][m-1])