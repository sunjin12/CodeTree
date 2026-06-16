import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    n = int(data[0])
    arr = [int(x) for x in data[1:n+1]]
    
    # 1. 앞에서부터 증가하는 LIS 구하기
    increase_dp = [1] * n
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                increase_dp[i] = max(increase_dp[i], increase_dp[j] + 1)
                
    # 2. 뒤에서부터 감소하는 LDS 구하기 (역방향 LIS)
    decrease_dp = [1] * n
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            if arr[j] < arr[i]:  # 뒤에 있는 원소(j)가 현재 원소(i)보다 작아야 감춤
                decrease_dp[i] = max(decrease_dp[i], decrease_dp[j] + 1)
                
    # 3. 각 정점별 (증가 길이 + 감소 길이 - 1) 중 최댓값 찾기
    max_len = 0
    for i in range(n):
        total_len = increase_dp[i] + decrease_dp[i] - 1
        max_len = max(max_len, total_len)
        
    print(max_len)

if __name__ == "__main__":
    solve()