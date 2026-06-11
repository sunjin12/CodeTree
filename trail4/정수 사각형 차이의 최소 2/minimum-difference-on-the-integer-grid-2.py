import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    
    # 격자에 존재하는 모든 고유한 숫자들을 추출 (최솟값 X의 후보들)
    unique_numbers = set()
    for r in range(N):
        for c in range(N):
            unique_numbers.add(grid[r][c])
            
    INF = float('inf')
    ans = INF
    
    # 1. 가능한 모든 최솟값 X에 대하여 DP를 반복 수행
    for X in unique_numbers:
        # 시작점 자체가 X보다 작다면 이 X는 최솟값이 될 수 없음
        if grid[0][0] < X:
            continue
            
        # DP 테이블 초기화
        dp = [[INF] * N for _ in range(N)]
        
        # 시작점 설정 (최솟값이 X일 때, 시작점의 최댓값은 곧 grid[0][0])
        dp[0][0] = grid[0][0]
        
        # 2. DP 테이블 채우기
        for r in range(N):
            for c in range(N):
                # 시작점은 이미 초기화했으므로 건너뜀
                if r == 0 and c == 0:
                    continue
                    
                # 현재 칸이 가정된 최솟값 X보다 작다면 방문 불가 (INF 유지)
                if grid[r][c] < X:
                    continue
                    
                # 위쪽 칸과 왼쪽 칸에서 오는 경로 중 최적의 값 선택
                from_top = dp[r-1][c] if r > 0 else INF
                from_left = dp[r][c-1] if c > 0 else INF
                
                min_prev_max = min(from_top, from_left)
                
                # 이전까지의 최댓값과 현재 칸의 숫자 중 더 큰 값이 새로운 최댓값
                if min_prev_max != INF:
                    dp[r][c] = max(min_prev_max, grid[r][c])
                    
        # 3. 우측 하단 끝에 도달 성공했다면 결과 갱신
        if dp[N-1][N-1] != INF:
            # (해당 경로의 최댓값 - 최솟값 X)의 최솟값을 정답으로 갱신
            current_diff = dp[N-1][N-1] - X
            ans = min(ans, current_diff)
            
    print(ans)

if __name__ == "__main__":
    solve()