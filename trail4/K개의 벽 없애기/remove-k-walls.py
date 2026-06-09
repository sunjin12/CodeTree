from collections import deque
from itertools import combinations
import sys

input = sys.stdin.readline


def bfs(start_r, start_c, end_r, end_c, current_grid, n):
    # 방문 여부 및 거리를 저장할 배열 (-1은 미방문)
    dist = [[-1] * n for _ in range(n)]
    queue = deque([(start_r, start_c)])
    dist[start_r][start_c] = 0

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while queue:
        r, c = queue.popleft()

        # 도착점에 도달했다면 거리 반환
        if r == end_r and c == end_c:
            return dist[r][c]

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < n and 0 <= nc < n:
                # 빈 칸(0)이거나 방문하지 않은 곳인 경우만 이동 가능
                if current_grid[nr][nc] == 0 and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))

    # 도착점에 도달할 수 없는 경우
    return -1


def solve():
    n, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    # 문제의 좌표가 1-index일 수 있으므로 입력받을 때 1을 빼서 0-index로 보정
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1

    # 1. 모든 벽의 위치를 찾음
    walls = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                walls.append((i, j))

    min_time = float("inf")
    possible = False

    # 2. k개의 벽을 고르는 모든 조합을 시험
    for k_walls in combinations(walls, k):
        # 원본 격자를 복사 (깊은 복사 대신 필요한 부분만 수정하기 위해 리스트 컴프리헨션 사용)
        test_grid = [row[:] for row in grid]

        # 선택된 k개의 벽을 허물기 (0으로 변경)
        for r, c in k_walls:
            test_grid[r][c] = 0

        # 3. BFS 실행
        result = bfs(r1, c1, r2, c2, test_grid, n)

        # 도달 가능한 경우 최솟값 갱신
        if result != -1:
            possible = True
            min_time = min(min_time, result)

    # 4. 정답 출력
    if possible:
        print(min_time)
    else:
        print(-1)


solve()