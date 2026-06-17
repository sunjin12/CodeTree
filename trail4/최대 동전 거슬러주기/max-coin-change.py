import sys

def solve():
    input = sys.stdin.readline
    
    # n: 동전의 종류 수, m: 목표 금액
    n, m = map(int, input().split())
    
    # 동전의 액면가 리스트
    coins = list(map(int, input().split()))
    
    # DP 테이블 초기화: 최댓값이므로 불가능한 상태를 -1로 표현합니다.
    dp = [-1] * (m + 1)
    
    # Base case: 0원을 만드는 데 필요한 최대 동전 수는 0개
    dp[0] = 0
    
    # 1번 문제처럼 동전을 중복해서 쓸 수 있으므로 1원부터 m원까지 순방향 탐색
    for i in range(1, m + 1):
        for coin in coins:
            # 금액 i가 동전 액면가보다 크거나 같고, 
            # i - coin 원을 만드는 조합이 존재하는 경우 (즉, -1이 아닌 경우)
            if i >= coin and dp[i - coin] != -1:
                dp[i] = max(dp[i], dp[i - coin] + 1)
                
    # 최종 결과 출력 (dp[m]이 여전히 -1이라면 거스름돈을 만들 수 없다는 뜻)
    print(dp[m])

if __name__ == "__main__":
    solve()