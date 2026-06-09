from collections import deque
import sys

input = sys.stdin.readline

# 1. 입력 받기
n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 방문 여부 및 대피소로부터의 거리를 저장할 배열 (-1은 미방문)
dist = [[-1] * n for _ in range(n)]
queue = deque()

# 2. 모든 대피소(3)의 위치를 시작점으로 설정하여 큐에 삽입
for i in range(n):
    for j in range(n):
        if grid[i][j] == 3:
            queue.append((i, j))  # (행, 열) 튜플 형태로 큐에 삽입
            dist[i][j] = 0  # 대피소 자체의 거리는 0

# 상하좌우 이동 방향 정의
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 3. 대피소들을 시작점으로 하는 단 한 번의 BFS 수행
while queue:
    r, c = queue.popleft()  # 정상적으로 (r, c) 두 개의 값을 꺼냅니다.

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        # 격자 범위 내에 있고, 벽(1)이 아닌 경우
        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] != 1:
            # 아직 방문하지 않은 경로라면 최단 거리 갱신
            if dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))

# 4. 정답 출력 배열 생성
answer = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        # 원래 사람이 있던 자리(2)인 경우에만 대피소까지의 거리를 기록
        if grid[i][j] == 2:
            answer[i][j] = dist[i][j]

# 결과 출력
for row in answer:
    print(*row)