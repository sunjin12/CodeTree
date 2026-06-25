import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    
    quests = []
    total_time = 0
    idx = 2
    for _ in range(n):
        e = int(data[idx])
        t = int(data[idx+1])
        quests.append((e, t))
        total_time += t
        idx += 2
        
    # dp[t]: 정확히 t시간을 써서 얻을 수 있는 최대 경험치
    # 존재할 수 없는 상태는 -1로 초기화
    dp = [-1] * (total_time + 1)
    dp[0] = 0
    
    current_max_time = 0
    
    for exp, time in quests:
        # 시간 합 상한선 계산 (최적화)
        next_max_time = current_max_time + time
        
        # 1차원 배낭 문제이므로 역순으로 탐색
        for t in range(current_max_time, -1, -1):
            if dp[t] == -1:
                continue
                
            if dp[t + time] < dp[t] + exp:
                dp[t + time] = dp[t] + exp
                
        current_max_time = next_max_time
        
    # 시간을 0부터 늘려가며 최초로 목표 경험치 M 이상을 달성하는 순간이 최소 시간
    ans = -1
    for t in range(total_time + 1):
        if dp[t] >= m:
            ans = t
            break
            
    print(ans)

if __name__ == '__main__':
    solve()