import sys

def solve():
    # 입력 받기
    n = int(sys.stdin.readline())
    
    # dp 배열 초기화 (0부터 n까지 저장하기 위해 n+1 크기)
    dp = [0] * (n + 1)
    
    # 초기값 설정
    dp[0] = 1
    dp[1] = 1
    
    # 2개부터 n개의 노드가 있을 때까지 차례대로 구하기
    for i in range(2, n + 1):
        # j는 루트 노드로 선택할 숫자의 상대적 위치 (1번째부터 i번째까지)
        for j in range(1, i + 1):
            # 왼쪽 서브트리 노드 수: j - 1
            # 오른쪽 서브트리 노드 수: i - j
            dp[i] += dp[j - 1] * dp[i - j]
            
    # 결과 출력
    print(dp[n])

if __name__ == "__main__":
    solve()