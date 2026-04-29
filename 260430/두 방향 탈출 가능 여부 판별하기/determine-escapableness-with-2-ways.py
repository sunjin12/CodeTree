import collections

# 1. 입력 받기
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 방문 체크 배열
visited = [[False] * m for _ in range(n)]

def solve():
    # 시작점이 0(뱀)이라면 바로 탈출 불가
    if grid[0][0] == 0:
        return 0
        
    queue = collections.deque([(0, 0)])
    visited[0][0] = True
    
    # ★ 문제의 핵심: 아래(1, 0)와 오른쪽(0, 1)만 가능
    dxs, dys = [1, 0], [0, 1]
    
    while queue:
        x, y = queue.popleft()
        
        # 목적지 도달 여부 확인
        if x == n - 1 and y == m - 1:
            return 1
            
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            # 격자 범위 체크
            if 0 <= nx < n and 0 <= ny < m:
                # 뱀이 없고(1), 아직 방문하지 않은 경우만 이동
                if grid[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    
    return 0

# 결과 출력
print(solve())