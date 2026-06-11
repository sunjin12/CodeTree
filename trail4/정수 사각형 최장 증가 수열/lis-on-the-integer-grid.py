import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    
    # 1. 모든 칸의 DP 값을 1로 초기화 (질문하신 내용!)
    dp = [[1] * N for _ in range(N)]
    
    # 2. 모든 위치를 (숫자, 행, 열) 형태로 리스트에 저장
    cells = []
    for r in range(N):
        for c in range(N):
            cells.append((grid[r][c], r, c))
            
    # 3. 숫자가 작은 칸부터 차례대로 방문하기 위해 오름차순 정렬 (★핵심)
    cells.sort()
    
    # 상하좌우 이동을 위한 방향 배열
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    # 4. 작은 숫자가 적힌 칸부터 순회하며 DP 갱신 (질문하신 핵심 로직!)
    for val, r, c in cells:
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            
            # 격자 범위 내에 있고, 주변 칸(nr, nc)이 현재 칸(r, c)보다 숫자가 작은 경우
            if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] < grid[r][c]:
                # 현재 칸의 DP 값을 (작은 칸의 DP 값 + 1) 중 최댓값으로 갱신
                dp[r][c] = max(dp[r][c], dp[nr][nc] + 1)
                
    # 5. 모든 DP 값 중 가장 큰 값이 격자 내에서 만들 수 있는 최장 경로입니다.
    ans = 0
    for r in range(N):
        for c in range(N):
            ans = max(ans, dp[r][c])
            
    print(ans)

if __name__ == "__main__":
    solve()