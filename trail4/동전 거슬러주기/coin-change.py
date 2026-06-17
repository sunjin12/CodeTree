import sys

def solve():
    # 입력 처리 (sys.stdin.readline은 입력 속도를 높여줍니다)
    input = sys.stdin.readline
    
    # n: 동전의 종류 수, m: 목표 금액
    n, m = map(int, input().split())
    
    # 동전의 액면가 리스트
    coins = list(map(int, input().split()))
    
    # DP 테이블 초기화: 거스름돈을 만들 수 없는 경우를 대비해 충분히 큰 값(INF)으로 설정
    # m의 최대 크기에 맞춰 INF를 설정하거나 float('inf')를 사용합니다.
    INF = float('inf')
    dp = [INF] * (m + 1)
    
    # Base case: 0원을 만드는 데 필요한 동전의 수는 0개
    dp[0] = 0
    
    # DP 테이블 채우기
    # 1원부터 m원까지 순차적으로 최소 동전 수를 구합니다.
    for i in range(1, m + 1):
        for coin in coins:
            # 현재 만들려는 금액 i가 동전의 액면가보다 크거나 같고,
            # i - coin 원을 만드는 방법이 존재하는 경우 (INF가 아닌 경우)
            if i >= coin and dp[i - coin] != INF:
                dp[i] = min(dp[i], dp[i - coin] + 1)
                
    # 최종 결과 출력
    # dp[m]이 여전히 INF라면 금액 m을 만드는 것이 불가능하다는 뜻입니다.
    if dp[m] == INF:
        print(-1)
    else:
        print(dp[m])

if __name__ == "__main__":
    solve()