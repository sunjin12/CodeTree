import sys

def solve():
    input = sys.stdin.readline
    n = int(input())
    
    MOD = 10007
    
    # dp[i]: 정수 i를 만드는 방법의 수
    dp = [0] * (n + 1)
    
    # Base case
    dp[0] = 1
    
    # 사용할 수 있는 숫자들
    numbers = [1, 2, 5]
    
    # 1원부터 n원까지 순방향으로 채우기 (중복 사용 가능하므로)
    for i in range(1, n + 1):
        for num in numbers:
            if i >= num:
                dp[i] = (dp[i] + dp[i - num]) % MOD
                
    print(dp[n])

if __name__ == "__main__":
    solve()