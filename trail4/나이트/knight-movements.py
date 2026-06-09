from collections import deque
import sys

input = sys.stdin.readline


def bfs():
    # 1. 입력 받기
    n = int(input())
    r1, c1, r2, c2 = map(int, input().split())

    # ★ 중요: 1-index 좌표를 0-index로 변환 (1씩 빼주기)
    r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1

    # 시작점과 도착점이 처음부터 같다면 0 출력
    if r1 == r2 and c1 == c2:
        return 0

    # 방문 여부와 이동 횟수를 기록할 격자
    visited = [[-1] * n for _ in range(n)]

    # 나이트의 8방향 이동 정의
    dr = [-2, -2, -1, -1, 1, 1, 2, 2]
    dc = [-1, 1, -2, 2, -2, 2, -1, 1]

    # 2. 시작 위치 설정
    queue = deque([(r1, c1)])
    visited[r1][c1] = 0

    while queue:
        r, c = queue.popleft()

        # 3. 8방향 탐색
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]

            # 격자 내에 있고 방문하지 않은 곳이라면
            if 0 <= nr < n and 0 <= nc < n:
                if visited[nr][nc] == -1:
                    visited[nr][nc] = visited[r][c] + 1

                    # 도착점에 도달했다면 정답 반환
                    if nr == r2 and nc == c2:
                        return visited[nr][nc]

                    queue.append((nr, nc))

    return -1


# 실행 및 출력
print(bfs())