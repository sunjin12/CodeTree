import sys

def solve():
    n = int(sys.stdin.readline())
    
    # n이 2나 3일 때를 대비한 예외 처리 및 배열 크기 설정
    if n == 2:
        print(1)
        return
    if n == 3:
        print(1)
        return
        
    # dp 배열 초기화 (인덱스 n까지 쓰기 위해 n+1 크기)
    dp = [0] * (n + 1)
    dp[2] = 1
    dp[3] = 1
    
    # 4번째 계단부터 n번째 계단까지 점화식 적용
    for i in range(4, n + 1):
        dp[i] = (dp[i - 2] + dp[i - 3]) % 10007
        
    print(dp[n])

solve()