import sys

def solve():
    # 빠른 입력을 위해 모든 데이터를 한 번에 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    # 1-indexed 구현을 위해 맨 앞에 0을 추가합니다.
    arr = [0] + [int(x) for x in input_data[2:2+N]]
    
    INF = float('inf')
    
    # dp[i][j][state] 테이블 초기화
    # i: 0~N, j: 0~M, state: 0(미포함/공백), 1(포함/구간진행중)
    dp = [[[-INF] * 2 for _ in range(M + 1)] for _ in range(N + 1)]
    
    # 기저 조건: 0번째 원소까지 원소를 하나도 안 고르고 0개 구간을 만든 합은 0
    dp[0][0][0] = 0
    
    for i in range(1, N + 1):
        # 구간을 0개 선택하고 i번째 원소도 안 고른 상태는 언제나 합이 0입니다.
        dp[i][0][0] = 0
        
        for j in range(1, M + 1):
            # 1. i번째 원소를 포함하지 않는 경우
            # 이전 원소가 안 뽑혔거나(0), 이전 원소를 끝으로 j번째 구간이 끝났거나(1)
            dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1])
            
            # 2. i번째 원소를 포함하는 경우
            # Case A: 기존 j번째 구간 연장 (이전 원소가 뽑혔던 상태여야 함)
            # Case B: 새 j번째 구간 시작 (이전 원소가 '공백'이었던 상태 dp[i-1][j-1][0]에서만 가능!)
            prev_max = max(dp[i-1][j][1], dp[i-1][j-1][0])
            
            if prev_max != -INF:
                dp[i][j][1] = arr[i] + prev_max

    # N번째 원소까지 탐색한 후, 정확히 M개의 구간을 완성한 두 상태 중 최댓값 선택
    ans = max(dp[N][M][0], dp[N][M][1])
    print(ans)

if __name__ == "__main__":
    solve()