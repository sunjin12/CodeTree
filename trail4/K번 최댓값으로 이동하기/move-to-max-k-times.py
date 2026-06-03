from collections import deque

# 1. 입력 받기
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# 0-index 기반으로 좌표 변경
current_r, current_c = r - 1, c - 1

# 상하좌우 이동을 위한 방향 벡터
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def find_next_position(start_r, start_c):
    """
    현재 위치에서 BFS를 수행하여 조건에 맞는 다음 위치를 반환합니다.
    이동할 곳이 없다면 None을 반환합니다.
    """
    target_value = grid[start_r][start_c]
    visited = [[False] * n for _ in range(n)]

    queue = deque([(start_r, start_c)])
    visited[start_r][start_c] = True

    # 이동 가능한 목적지들을 담을 리스트
    candidates = []

    while queue:
        curr_r, curr_c = queue.popleft()

        for i in range(4):
            nr, nc = curr_r + dr[i], curr_c + dc[i]

            # 격자 범위 내에 있고, 방문하지 않았으며, 시작 위치의 값보다 작은 경우만 이동 가능
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                if grid[nr][nc] < target_value:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
                    # 후보군에 (격자 값, 행, 열) 정보 저장
                    candidates.append((grid[nr][nc], nr, nc))

    if not candidates:
        return None

    # 우선순위 정렬 규칙:
    # 1. 격자 값은 클수록 (내림차순: -x[0])
    # 2. 행 번호는 작을수록 (오름차순: x[1])
    # 3. 열 번호는 작을수록 (오름차순: x[2])
    candidates.sort(key=lambda x: (-x[0], x[1], x[2]))

    # 최적의 후보의 (행, 열) 반환
    return candidates[0][1], candidates[0][2]


# 2. K번 반복 수행
for _ in range(k):
    next_pos = find_next_position(current_r, current_c)

    # 더 이상 이동할 수 있는 곳이 없다면 즉시 종료
    if next_pos is None:
        break

    current_r, current_c = next_pos

# 3. 결과 출력 (1-index 기반으로 다시 복원)
print(current_r + 1, current_c + 1)