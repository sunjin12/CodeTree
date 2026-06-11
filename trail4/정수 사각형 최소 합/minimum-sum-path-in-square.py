import sys

def solve():
    # 1. 입력 받기
    input = sys.stdin.readline
    N = int(input())
    
    # grid: 입력받은 격자 숫자판
    grid = [list(map(int, input().split())) for _ in range(N)]
    
    # dp: 최솟값을 누적할 DP 테이블 (N x N 크기를 0으로 초기화)
    dp = [[0] * N for _ in range(N)]
    
    # 2. 초기값 설정 (시작점: 우측 상단 끝)
    dp[0][N-1] = grid[0][N-1]
    
    # 3. 예외 처리: 맨 오른쪽 열 채우기 (위에서 아래로만 이동 가능)
    for r in range(1, N):
        dp[r][N-1] = dp[r-1][N-1] + grid[r][N-1]
        
    # 4. 예외 처리: 맨 첫 번째 행 채우기 (오른쪽에서 왼쪽으로만 이동 가능)
    # 인덱스가 N-2부터 0까지 1씩 감소합니다.
    for c in range(N-2, -1, -1):
        dp[0][c] = dp[0][c+1] + grid[0][c]
        
    # 5. 나머지 점화식 채우기 (행은 위->아래, 열은 오른쪽->왼쪽 순서)
    for r in range(1, N):
        for c in range(N-2, -1, -1):
            # 위쪽에서 내려오는 값과 오른쪽에서 오는 값 중 최소 선택 + 현재 위치의 값
            dp[r][c] = min(dp[r-1][c], dp[r][c+1]) + grid[r][c]
            
    # 6. 정답 출력 (좌측 하단 끝의 결과)
    print(dp[N-1][0])

if __name__ == "__main__":
    solve()