import sys
from collections import deque
from itertools import combinations

def solve():
    # 입력 받기
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    n = int(data[0])
    k = int(data[1])
    u = int(data[2])
    d = int(data[3])
    
    # 격자 정보 저장
    grid = []
    idx = 4
    for _ in range(n):
        grid.append([int(x) for x in data[idx:idx+n]])
        idx += n
        
    # 모든 칸의 좌표를 리스트에 담기 (조합을 구하기 위함)
    all_positions = [(r, c) for r in range(n) for c in range(n)]
    
    # 상하좌우 방향 벡터
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    max_accessible_cities = 0
    
    # 1. N*N 개의 칸 중 K개를 고르는 조합 순회
    for starts in combinations(all_positions, k):
        # 방문 여부 체크 배열 (매 조합마다 새로 초기화)
        visited = [[False] * n for _ in range(n)]
        queue = deque()
        
        # 선택된 K개의 시작점을 모두 큐에 넣고 방문 처리
        visited_count = 0
        for r, c in starts:
            queue.append((r, c))
            visited[r][c] = True
            visited_count += 1
            
        # 2. BFS 탐색 시작
        while queue:
            curr_r, curr_c = queue.popleft()
            
            for i in range(4):
                nr = curr_r + dr[i]
                nc = curr_c + dc[i]
                
                # 격자 범위 내에 있고 아직 방문하지 않은 경우
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    # 높이 차이 조건 확인 (U 이상 D 이하)
                    height_diff = abs(grid[curr_r][curr_c] - grid[nr][nc])
                    if u <= height_diff <= d:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
                        visited_count += 1
                        
        # 3. 갈 수 있는 최대 도시 수 갱신
        if visited_count > max_accessible_cities:
            max_accessible_cities = visited_count
            
    # 정답 출력
    print(max_accessible_cities)

if __name__ == '__main__':
    solve()