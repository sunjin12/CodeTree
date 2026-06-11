import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    
    # DP 테이블 초기화
    dp = [[0] * N for _ in range(N)]
    
    # 1. 시작점 설정
    dp[0][0] = grid[0][0]
    
    # 2. 맨 첫 번째 열 채우기 (위 -> 아래)
    for r in range(1, N):
        dp[r][0] = min(dp[r-1][0], grid[r][0])
        
    # 3. 맨 첫 번째 행 채우기 (왼쪽 -> 오른쪽)
    for c in range(1, N):
        dp[0][c] = min(dp[0][c-1], grid[0][c])
        
    # 4. 나머지 칸 채우기
    for r in range(1, N):
        for c in range(1, N):
            # 위와 왼쪽 중 더 나은 경로(max)를 선택하고, 현재 칸의 값과 비교해 최솟값(min)을 구함
            best_prev = max(dp[r-1][c], dp[r][c-1])
            dp[r][c] = min(best_prev, grid[r][c])
            
    # 5. 우측 하단 끝의 결과 출력
    print(dp[N-1][0] if N == 1 else dp[N-1][N-1])

if __name__ == "__main__":
    solve()