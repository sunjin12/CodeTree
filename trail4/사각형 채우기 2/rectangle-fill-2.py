import sys

def solve():
    n = int(sys.stdin.readline())
    
    # n이 1일 때의 예외 처리
    if n == 1:
        print(1)
        return
        
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 3
    
    # 3부터 n까지 점화식 적용
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % 10007
        
    print(dp[n])

solve()