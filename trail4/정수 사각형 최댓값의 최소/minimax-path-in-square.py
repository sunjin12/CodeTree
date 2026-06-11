import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    
    # 최솟값을 골라 나가야 하므로 초기값은 아주 큰 값(INF)으로 채웁니다.
    INF = float('inf')
    dp = [[INF] * N for _ in range(N)]
    
    # 1. 시작점 설정 (시작 칸의 최댓값은 곧 시작 칸의 숫자 자체입니다)
    dp[0][0] = grid[0][0]
    
    # 2. DP 테이블 채우기
    for r in range(N):
        for c in range(N):
            # 시작점은 이미 계산했으므로 건너뜁니다.
            if r == 0 and c == 0:
                continue
                
            # 위쪽 칸과 왼쪽 칸에서 오는 경로의 최댓값 가져오기 (경계선 예외 처리)
            from_top = dp[r-1][c] if r > 0 else INF
            from_left = dp[r][c-1] if c > 0 else INF
            
            # 둘 중 더 유리한(최댓값이 더 작은) 경로를 고릅니다.
            best_prev_max = min(from_top, from_left)
            
            # 고른 경로의 최댓값과 현재 칸의 숫자 중 더 큰 값이 현재 칸의 DP 값이 됩니다.
            dp[r][c] = max(best_prev_max, grid[r][c])
            
    # 3. 우측 하단 끝의 최적 결과 출력
    print(dp[N-1][N-1])

if __name__ == "__main__":
    solve()