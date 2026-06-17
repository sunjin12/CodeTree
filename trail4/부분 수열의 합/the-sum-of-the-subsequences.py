import sys

def solve():
    input = sys.stdin.readline
    
    # n: 원소의 개수, m: 목표 합
    n, m = map(int, input().split())
    
    # 수열 입력
    arr = list(map(int, input().split()))
    
    # dp[i]: 합 i를 만들 수 있는지 여부 (Boolean 테이블)
    dp = [False] * (m + 1)
    
    # Base case: 합이 0인 경우는 항상 가능
    dp[0] = True
    
    # 각 원소를 하나씩 순회 (중복 선택 불가)
    for num in arr:
        # 중복 사용을 막기 위해 m부터 num까지 역순(거꾸로) 탐색!
        for i in range(m, num - 1, -1):
            if dp[i - num]:
                dp[i] = True
                
    # 최종 결과 출력
    # 문제 요구사항이 "가능하면 Yes, 불가능하면 No"라면 아래와 같이 처리합니다.
    if dp[m]:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    solve()