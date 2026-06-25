import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
    
    n = int(data[0])
    arr = [int(x) for x in data[1:n+1]]
    
    total_sum = sum(arr)
    # 차이(j)의 범위는 -total_sum 부터 +total_sum 까지 가능합니다.
    OFFSET = total_sum
    MAX_J = 2 * total_sum
    
    # 존재할 수 없는 상태는 -1로 초기화
    dp = [-1] * (MAX_J + 1)
    # 시작 상태: 0번째까지 봤을 때 차이가 0인 경우, A그룹의 합은 0
    dp[0 + OFFSET] = 0
    
    for x in arr:
        # 이전 단계의 DP 테이블을 복사해서 사용 (차례대로 갱신할 때의 간섭 방지)
        next_dp = dp[:]
        
        for j in range(MAX_J + 1):
            if dp[j] == -1:
                continue
                
            # 1. A 그룹에 원소 x를 추가하는 경우
            if j + x <= MAX_J:
                next_dp[j + x] = max(next_dp[j + x], dp[j] + x)
                
            # 2. B 그룹에 원소 x를 추가하는 경우
            if j - x >= 0:
                next_dp[j - x] = max(next_dp[j - x], dp[j])
                
        dp = next_dp
        
    # 최종적으로 두 그룹의 합이 같은 경우 = 차이가 0인 경우 (j = 0 + OFFSET)
    # 만약 dp[OFFSET]이 여전히 -1이거나 0이면 두 그룹으로 분할이 불가능하거나 합이 0인 경우입니다.
    print(dp[OFFSET])

if __name__ == '__main__':
    solve()