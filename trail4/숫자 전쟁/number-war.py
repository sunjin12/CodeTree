import sys

# 재귀 깊이 제한 해제
sys.setrecursionlimit(10**6)

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    N = int(data[0])
    # A: 첫 번째 플레이어(상대방), B: 두 번째 플레이어(남우)
    A = [int(x) for x in data[1:N+1]]
    B = [int(x) for x in data[N+1:2*N+1]]
    
    # dp[i][j] : 상대 i번째, 남우 j번째 카드 상황에서 얻을 수 있는 최대 점수
    dp = [[-1] * N for _ in range(N)]
    
    def get_max_score(i, j):
        # 기저 조건: 어느 한쪽이라도 카드를 다 쓰면 종료
        if i == N or j == N:
            return 0
        
        # 이미 계산한 결과가 있다면 재활용
        if dp[i][j] != -1:
            return dp[i][j]
        
        # 1. 상대 카드가 더 큰 경우 -> 남우가 점수를 획득하고 남우 카드만 버려짐
        if A[i] > B[j]:
            # 대결하기 vs 카드 버리기 중 최댓값 (사실 대결하기가 항상 이득)
            dp[i][j] = max(get_max_score(i, j + 1) + B[j], get_max_score(i + 1, j + 1))
            
        # 2. 남우 카드가 더 큰 경우 -> 대결 시 상대 카드만 버려짐 (남우 점수 0)
        elif A[i] < B[j]:
            # 대결하기(상대만 버리기) vs 카드 버리기(둘 다 버리기)
            # 카드를 아끼는 상대만 버리기가 항상 유리합니다.
            dp[i][j] = max(get_max_score(i + 1, j), get_max_score(i + 1, j + 1))
            
        # 3. 두 카드가 같은 경우 -> 어떤 선택을 하든 둘 다 버려짐 (점수 0)
        else:
            dp[i][j] = get_max_score(i + 1, j + 1)
            
        return dp[i][j]

    print(get_max_score(0, 0))

if __name__ == '__main__':
    solve()