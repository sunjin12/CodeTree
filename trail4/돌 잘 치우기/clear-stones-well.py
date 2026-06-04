from collections import deque
from itertools import combinations

# 1. 입력 받기
n, k, m = map(int, input().split())

grid = []
stones = []  # 모든 돌의 위치를 저장할 리스트

for r in range(n):
    row = list(map(int, input().split()))
    grid.append(row)
    for c in range(n):
        if row[c] == 1:
            stones.append((r, c))

# 시작점 위치 입력 받기 (0-indexed로 변경)
start_points = []
for _ in range(k):
    sr, sc = map(int, input().split())
    start_points.append((sr - 1, sc - 1))

# 상하좌우 방향 배열
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 2. BFS 탐색 함수 정의
def get_visited_count(removed_stones):
    # 기존 격자를 복사하여 사용 (돌을 치운 상태 반영)
    # 0: 빈칸, 1: 돌
    temp_grid = [row[:] for row in grid]
    for r, c in removed_stones:
        temp_grid[r][c] = 0 # 선택한 돌은 빈칸으로 변경
        
    queue = deque()
    visited = [[False] * n for _ in range(n)]
    
    # 모든 시작점을 큐에 삽입하고 방문 처리
    for sr, sc in start_points:
        queue.append((sr, sc))
        visited[sr][sc] = True
        
    count = k # 초기 방문 칸 수 (시작점 개수만큼)
    
    while queue:
        r, c = queue.popleft()
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            # 격자 범위 내에 있고, 아직 방문하지 않았으며, 벽(돌)이 없는 경우
            if 0 <= nr < n and 0 <= nc < n:
                if not visited[nr][nc] and temp_grid[nr][nc] == 0:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
                    count += 1
                    
    return count

# 3. 모든 조합을 시도하며 최댓값 찾기
max_accessible = 0

# stones 중에서 m개를 뽑는 모든 조합 순회
for removed in combinations(stones, m):
    current_count = get_visited_count(removed)
    max_accessible = max(max_accessible, current_count)

# 4. 결과 출력
print(max_accessible)