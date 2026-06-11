import sys

def solve():
    n = int(sys.stdin.readline())
    
    if n == 1:
        print(1)
        return
    if n == 2:
        print(2)
        return
        
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        # 문제 조건에 있는 10007 나머지 연산을 잊지 마세요!
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007
        
    print(dp[n])

solve()