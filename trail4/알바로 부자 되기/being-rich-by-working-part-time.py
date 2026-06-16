import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    n = int(data[0])
    
    # 알바 정보 입력 받기 (시작일, 종료일, 수익)
    jobs = []
    idx = 1
    for _ in range(n):
        s = int(data[idx])
        e = int(data[idx+1])
        p = int(data[idx+2]) # profit (수익)
        jobs.append((s, e, p))
        idx += 3
        
    # 1. 시작일 기준 오름차순 정렬
    jobs.sort()
    
    # 2. dp 배열 초기화 (각 알바를 단독으로 할 때 벌 수 있는 수익으로 세팅)
    dp = [0] * n
    for i in range(n):
        dp[i] = jobs[i][2] # 각 알바의 기본 수익
        
    # 3. DP 수행 (O(N^2))
    for i in range(1, n):
        curr_start, curr_end, curr_profit = jobs[i]
        
        for j in range(i):
            prev_start, prev_end, prev_profit = jobs[j]
            
            # 이전 알바의 종료일이 현재 알바의 시작일보다 먼저 끝난다면 겹치지 않음
            # (만약 당일 종료 후 당일 시작이 가능하면 <= 로 수정해야 할 수 있습니다.)
            if prev_end < curr_start:
                dp[i] = max(dp[i], dp[j] + curr_profit)
                
    # 4. 모든 경우 중 벌 수 있는 최대 수익 출력
    print(max(dp))

if __name__ == "__main__":
    solve()