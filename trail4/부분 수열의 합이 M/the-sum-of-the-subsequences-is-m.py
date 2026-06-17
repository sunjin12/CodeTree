import sys

def solve():
    input = sys.stdin.readline
    
    # n: 원소의 개수, m: 목표 합
    n, m = map(int, input().split())
    
    # 수열 입력
    arr = list(map(int, input().split()))
    
    # DP 테이블 초기화 (최소 길이를 구하므로 INF로 설정)
    INF = float('inf')
    dp = [INF] * (m + 1)
    
    # Base case: 합이 0일 때의 부분 수열의 최소 길이는 0
    dp[0] = 0
    
    # 각 원소를 하나씩 순회 (중복 선택 불가)
    for num in arr:
        # m원부터 num원까지 역순으로 조사!!
        for i in range(m, num - 1, -1):
            if dp[i - num] != INF:
                dp[i] = min(dp[i], dp[i - num] + 1)
                
    # 결과 출력
    if dp[m] == INF:
        print(-1)
    else:
        print(dp[m])

if __name__ == "__main__":
    solve()