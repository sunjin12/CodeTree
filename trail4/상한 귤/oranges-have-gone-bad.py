from collections import deque
import sys

input = sys.stdin.readline

# 1. 입력 받기
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 각 칸이 상하는 데 걸리는 시간을 기록할 배열 (-1로 초기화)
dist = [[-1] * n for _ in range(n)]
queue = deque()

# 2. 처음부터 상해 있던 귤(2)을 모두 큐에 삽입하고 시간 0 세팅
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            queue.append((i, j))
            dist[i][j] = 0

# 상하좌우 이동 방향
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 3. 다중 시작점 BFS 수행 (상한 귤이 동시에 퍼짐)
while queue:
    r, c = queue.popleft()

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        # 격자 범위 내에 있고
        if 0 <= nr < n and 0 <= nc < n:
            # 싱싱한 귤(1)이며, 아직 상하지 않은(방문하지 않은) 곳이라면
            if grid[nr][nc] == 1 and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))

# 4. 문제 조건에 맞게 출력 배열 가공
for i in range(n):
    for j in range(n):
        # 원래 귤이 없던 칸(0) -> -1 출력
        if grid[i][j] == 0:
            grid[i][j] = -1
        # 원래 싱싱한 귤(1)이었으나 끝내 상하지 못한 칸 -> -2 출력
        elif grid[i][j] == 1 and dist[i][j] == -1:
            grid[i][j] = -2
        # 상한 귤이 있는 칸 -> 걸린 시간 출력
        else:
            grid[i][j] = dist[i][j]

# 결과 출력
for row in grid:
    print(*row)