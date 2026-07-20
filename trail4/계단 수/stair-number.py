import sys

def solve():
    N = int(sys.stdin.readline())
    MOD = 1000000007  # 코드트리 문제 기준 모듈러 값 (문제 조건에 따라 변형 가능)

    # dp[i][j] : 길이가 i이고 끝자리가 j인 계단 수의 개수
    dp = [[0] * 10 for _ in range(N + 1)]

    # 1자릿수 초기화 (0으로 시작할 수는 없으므로 1~9만 1로 설정)
    for j in range(1, 10):
        dp[1][j] = 1

    # 2자릿수부터 N자릿수까지 DP 진행
    for i in range(2, N + 1):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i - 1][1] % MOD
            elif j == 9:
                dp[i][j] = dp[i - 1][8] % MOD
            else:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % MOD

    # N자릿수 계단 수의 총합 계산
    ans = sum(dp[N]) % MOD
    print(ans)

if __name__ == '__main__':
    solve()