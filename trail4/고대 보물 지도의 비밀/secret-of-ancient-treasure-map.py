import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    n = int(data[0])
    k = int(data[1])
    nums = [int(x) for x in data[2:2+n]]
    
    INF = float('inf')
    # dp[i][j]: i번째 원소를 마지막으로 포함하고, 음수가 j개인 연속합의 최댓값
    dp = [[-INF] * (k + 1) for _ in range(n)]
    
    # 첫 번째 원소 초기화
    if nums[0] >= 0:
        dp[0][0] = nums[0]
    else:
        if k >= 1:
            dp[0][1] = nums[0]
            
    ans = nums[0] # 최소 하나의 원소는 골라야 하므로 첫 값으로 초기화
    
    for i in range(1, n):
        current = nums[i]
        
        if current >= 0:
            for j in range(k + 1):
                # 1. 이전 연속 수열에 이어 붙이기
                if dp[i-1][j] != -INF:
                    dp[i][j] = max(dp[i][j], dp[i-1][j] + current)
            # 2. 현재 원소부터 새로 수열 시작 (음수 개수 = 0)
            dp[i][0] = max(dp[i][0], current)
            
        else: # 음수인 경우
            for j in range(1, k + 1):
                # 1. 이전 연속 수열에 이어 붙이기 (음수 개수가 j-1개였던 상태에서 연결)
                if dp[i-1][j-1] != -INF:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1] + current)
            # 2. 현재 원소부터 새로 수열 시작 (음수 개수 = 1)
            if k >= 1:
                dp[i][1] = max(dp[i][1], current)
                
        # 매 원소마다 가능한 모든 j(음수 개수) 상태 중 최댓값을 갱신
        for j in range(k + 1):
            if dp[i][j] > ans:
                ans = dp[i][j]
                
    print(ans)

if __name__ == "__main__":
    solve()