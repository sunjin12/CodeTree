import sys

def solve():
    # 표준 입력으로부터 N을 입력받습니다.
    input = sys.stdin.read
    N = int(input().strip())
    
    MOD = 10**9 + 7
    
    # dp[t][b]: 총 T의 개수가 t개(0~2), 연속 B의 개수가 b개(0~2)인 경우의 수
    dp = [[0] * 3 for _ in range(3)]
    
    # 0일차 초기 상태: T는 0개, 연속 B도 0개인 상태가 1가지 존재
    dp[0][0] = 1
    
    # N일 동안 반복
    for _ in range(N):
        # 다음 날의 상태를 저장할 임시 DP 테이블 초기화
        next_dp = [[0] * 3 for _ in range(3)]
        
        for t in range(3):
            for b in range(3):
                if dp[t][b] == 0:
                    continue
                
                current_cnt = dp[t][b]
                
                # 1. 'G'를 고르는 경우 -> 총 T 유지, 연속 B는 0으로 리셋
                next_dp[t][0] = (next_dp[t][0] + current_cnt) % MOD
                
                # 2. 'B'를 고르는 경우 -> 총 T 유지, 연속 B는 1 증가 (3 미만일 때만)
                if b + 1 < 3:
                    next_dp[t][b + 1] = (next_dp[t][b + 1] + current_cnt) % MOD
                    
                # 3. 'T'를 고르는 경우 -> 총 T는 1 증가 (3 미만일 때만), 연속 B는 0으로 리셋
                if t + 1 < 3:
                    next_dp[t + 1][0] = (next_dp[t + 1][0] + current_cnt) % MOD
        
        # 다음 날의 테이블을 현재 테이블로 업데이트
        dp = next_dp
        
    # N일이 지난 후, 해고당하지 않은 모든 생존 상태의 경우의 수를 더함
    ans = 0
    for t in range(3):
        for b in range(3):
            ans = (ans + dp[t][b]) % MOD
            
    print(ans)

if __name__ == "__main__":
    solve()