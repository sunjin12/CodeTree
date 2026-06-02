import sys
from collections import deque

# 1. 입력 받기
n = int(sys.stdin.readline().strip())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 방문 여부를 체크할 배열
visited = [[False] * n for _ in range(n)]

# 상하좌우 방향 배열
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(start_r, start_c, target_num):
    """
    (start_r, start_c)에서 시작해서 target_num과 같은 숫자로 이루어진
    블록의 크기(칸의 개수)를 반환하는 BFS 함수
    """
    queue = deque([(start_r, start_c)])
    visited[start_r][start_c] = True
    block_size = 1  # 시작점 포함하므로 1부터 시작
    
    while queue:
        r, c = queue.popleft()
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            # 격자 범위를 벗어나지 않고, 방문한 적이 없으며, 시작점의 숫자와 같은 경우
            if 0 <= nr < n and 0 <= nc < n:
                if not visited[nr][nc] and grid[nr][nc] == target_num:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
                    block_size += 1
                    
    return block_size

# 정답을 저장할 변수 초기화
total_pop_blocks = 0   # 터지게 되는 블록의 총 수 (크기가 4 이상인 블록 수)
max_block_size = 0     # 터지든 안 터지든 격자 내 모든 블록 중 최대 크기

# 2. 격자 전체를 순회하며 탐색 진행
for r in range(n):
    for c in range(n):
        if not visited[r][c]:
            # 새로운 블록을 발견하면 BFS 탐색 시작
            current_size = bfs(r, c, grid[r][c])
            
            # 조건 1: 블록의 크기가 4 이상이면 터짐
            if current_size >= 4:
                total_pop_blocks += 1
                
            # 조건 2: 최대 블록 크기 갱신 (크기가 4 미만이어도 최대 크기가 될 수 있음)
            max_block_size = max(max_block_size, current_size)

# 3. 결과 출력
print(total_pop_blocks, max_block_size)