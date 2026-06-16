import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    n = int(data[0])
    m = int(data[1]) # 만약 N x M 행렬이라면
    
    grid = []
    idx = 2
    for r in range(n):
        grid.append([int(x) for x in data[idx:idx+m]])
        idx += m
        
    # 1. 모든 칸의 정보를 (값, r, c)로 모으기
    cells = []
    for r in range(n):
        for c in range(m):
            cells.append((grid[r][c], r, c))
            
    # 2. 값 기준 오름차순 정렬 (값이 작은 것부터 처리해야 DP 보장)
    cells.sort()
    
    # dp[r][c]: (r, c) 칸에 도달했을 때의 최대 이동 횟수 (시작 칸을 0 또는 1로 설정)
    # 시작점 (0,0) 이외에는 일단 도달할 수 없으므로 -1 등으로 초기화
    dp = [[-1] * m for _ in range(n)]
    dp[0][0] = 1 # 시작점의 밟은 칸 수 (문제 조건에 따라 0 또는 1)
    
    # 3. 정렬된 순서대로 DP 갱신
    for val, r, c in cells:
        # 도달할 수 없는 칸에서 출발할 수는 없음
        if dp[r][c] == -1: 
            continue
            
        # 현재 칸(r, c)에서 다음 칸(nr, nc)으로 점프할 수 있는 곳 탐색
        # 문제 조건: 오른쪽 아래 방향으로만 점프 (nr > r, nc > c)
        for nr in range(r + 1, n):
            for nc in range(c + 1, m):
                # 조건: 다음 칸의 숫자가 현재 칸의 숫자보다 엄격히 커야 함
                if grid[nr][nc] > val:
                    dp[nr][nc] = max(dp[nr][nc], dp[r][c] + 1)
                    
    # 모든 칸 중 DP 최대값 찾기
    ans = 0
    for r in range(n):
        for c in range(m):
            ans = max(ans, dp[r][c])
            
    print(ans)

if __name__ == "__main__":
    solve()