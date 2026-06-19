import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    # N: 물건의 개수, M: 배낭의 최대 무게
    N = int(data[0])
    M = int(data[1])
    
    # dp[j]: 무게 j일 때 얻을 수 있는 최대 가치
    dp = [0] * (M + 1)
    
    idx = 2
    for _ in range(N):
        w = int(data[idx])      # 물건의 무게
        v = int(data[idx+1])    # 물건의 가치
        idx += 2
        
        # 1차원 DP에서는 뒤에서부터 앞으로 채워야 이전 아이템의 값이 덮어써지지 않습니다.
        for j in range(M, w - 1, -1):
            dp[j] = max(dp[j], dp[j - w] + v)
            
    # 배낭 무게 M일 때의 최대 가치 출력
    print(dp[M])

if __name__ == '__main__':
    solve()