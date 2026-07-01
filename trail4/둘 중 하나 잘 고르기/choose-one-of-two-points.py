import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    n = int(data[0])
    cards = []
    
    # 2N개의 카드 쌍 입력받기
    idx = 1
    for _ in range(2 * n):
        red = int(data[idx])
        blue = int(data[idx+1])
        cards.append((red, blue))
        idx += 2
        
    INF = float('inf')
    # dp[i][j]: i번째 카드까지 고려했을 때, 첫 번째(red)를 j개 골랐을 때의 최대 합
    dp = [[-INF] * (n + 1) for _ in range(2 * n + 1)]
    
    # 초기 상태
    dp[0][0] = 0
    
    # DP 테이블 채우기
    for i in range(1, 2 * n + 1):
        red, blue = cards[i-1] # 0-indexed로 가져옴
        
        for j in range(n + 1):
            # 1. 이번에 두 번째 값(blue)을 고르는 경우 (이전까지 red를 j개 골랐음)
            if dp[i-1][j] != -INF:
                dp[i][j] = max(dp[i][j], dp[i-1][j] + blue)
                
            # 2. 이번에 첫 번째 값(red)을 고르는 경우 (이전까지 red를 j-1개 골랐음)
            if j > 0 and dp[i-1][j-1] != -INF:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + red)
                
    # 정확히 red N개, blue N개를 고른 최종 결과 출력
    print(dp[2 * n][n])

if __name__ == "__main__":
    solve()