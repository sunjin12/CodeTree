import sys

def solve():
    n = int(sys.stdin.readline())
    MOD = 1000000007
    
    # 예외 처리
    if n == 1:
        print(2)
        return
    if n == 2:
        print(7)
        return
        
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 2
    dp[2] = 7
    
    for i in range(3, n + 1):
        # f(n) = 3 * f(n-1) + f(n-2) - f(n-3)
        # 음수가 나오는 것을 방지하기 위해 MOD를 더해줍니다.
        dp[i] = (3 * dp[i - 1] + dp[i - 2] - dp[i - 3] + MOD) % MOD
        
    print(dp[n])

solve()