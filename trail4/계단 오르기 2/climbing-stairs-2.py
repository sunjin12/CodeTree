import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    n = int(data[0])
    # 문제에서 1칸 오르기는 최대 3번으로 고정됨
    MAX_M = 3
    
    coins = [0] + list(map(int, data[1:1+n]))
    
    # dp[i][j]: i번째 계단까지 1칸 오르기를 j번(0~3번) 사용했을 때의 최댓값
    # 도달할 수 없는 상태는 -1로 초기화
    dp = [[-1] * (MAX_M + 1) for _ in range(n + 1)]
    
    # 시작점 (0번째 계단, 1칸 오르기 0번 사용)
    dp[0][0] = 0
    
    # 1번째 계단 초기화 (0번에서 1칸 오르는 방법뿐이므로 1칸 오르기 횟수 1 증가)
    dp[1][1] = coins[1]
        
    # 2번째 계단부터 DP 테이블 채우기
    for i in range(2, n + 1):
        for j in range(4): # 0, 1, 2, 3번 사용한 경우를 조사
            # 1. 2칸 밑에서 올라오는 경우 (1칸 오르기 횟수 변화 없음)
            if dp[i-2][j] != -1:
                dp[i][j] = max(dp[i][j], dp[i-2][j] + coins[i])
                
            # 2. 1칸 밑에서 올라오는 경우 (1칸 오르기 횟수가 이전보다 1번 늘어남)
            if j > 0 and dp[i-1][j-1] != -1:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + coins[i])
                
    # n번째 계단에서 1칸 오르기를 0, 1, 2, 3번 쓴 것 중 최댓값 구하기
    ans = max(dp[n])
    
    print(ans)

if __name__ == "__main__":
    solve()