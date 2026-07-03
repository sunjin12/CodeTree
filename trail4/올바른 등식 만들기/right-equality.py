import sys

def solve():
    input = sys.stdin.readline
    
    # N: 숫자의 개수, M: 목표 결과값
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    
    # 값의 범위가 -20 ~ 20이므로, 배열 인덱스 음수 처리를 위한 BASE
    BASE = 20
    MAX_VAL = 20
    MIN_VAL = -20
    
    # dp[i][j]: i번째 숫자까지 연산했을 때, 결과가 (j - BASE)가 되는 경우의 수
    dp = [[0] * 41 for _ in range(n)]
    
    # [초기 조건] 첫 번째 숫자(nums[0]) 앞에도 + 또는 -를 붙일 수 있습니다.
    first_num = nums[0]
    
    # 1. 첫 번째 숫자에 +를 붙이는 경우
    if MIN_VAL <= first_num <= MAX_VAL:
        dp[0][first_num + BASE] += 1
        
    # 2. 첫 번째 숫자에 -를 붙이는 경우 (단, 0인 경우는 중복 방지를 위해 조건 분기)
    if MIN_VAL <= -first_num <= MAX_VAL:
        dp[0][-first_num + BASE] += 1

    # DP 진행 (두 번째 숫자부터 끝까지)
    for i in range(1, n):
        current_num = nums[i]
        for j in range(MIN_VAL, MAX_VAL + 1):
            if dp[i-1][j + BASE] > 0:
                # 1. 현재 숫자를 더하는 경우
                if MIN_VAL <= j + current_num <= MAX_VAL:
                    dp[i][j + current_num + BASE] += dp[i-1][j + BASE]
                # 2. 현재 숫자를 빼는 경우
                if MIN_VAL <= j - current_num <= MAX_VAL:
                    dp[i][j - current_num + BASE] += dp[i-1][j + BASE]

    # N개의 숫자를 모두 사용해 M을 만드는 경우의 수 출력
    print(dp[n-1][m + BASE])

if __name__ == "__main__":
    solve()