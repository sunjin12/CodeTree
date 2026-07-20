import sys

def solve():
    # N: 옷의 개수, M: 날짜 수
    N, M = map(int, sys.stdin.readline().split())
    
    clothes = []
    for _ in range(N):
        # s: 시작일, e: 종료일, v: 화려함
        s, e, v = map(int, sys.stdin.readline().split())
        clothes.append((s, e, v))
        
    # dp[i][j] : i번째 날(1~M)에 j번 옷(0~N-1)을 입었을 때의 최대 만족도
    dp = [[-1] * N for _ in range(M + 1)]
    
    # 1일 차 초기화
    for j in range(N):
        s, e, v = clothes[j]
        if s <= 1 <= e:
            dp[1][j] = 0  # 1일 차에는 옷만 입고 아직 만족도 차이는 없음

    # 2일 차부터 M일 차까지 DP 진행
    for i in range(2, M + 1):
        for j in range(N):
            s_j, e_j, v_j = clothes[j]
            
            # 오늘(i일) j번 옷을 입을 수 있는 날인지 확인
            if not (s_j <= i <= e_j):
                continue
                
            # 어제(i-1일) 입었던 k번 옷 탐색
            for k in range(N):
                # 어제 k번 옷을 입은 경우가 유효한 경우만 계산
                if dp[i - 1][k] != -1:
                    v_k = clothes[k][2]
                    satisfaction_gain = abs(v_j - v_k)
                    dp[i][j] = max(dp[i][j], dp[i - 1][k] + satisfaction_gain)

    # M일 차에 입을 수 있었던 모든 옷들 중 최댓값 구하기
    ans = max(dp[M])
    print(ans)

if __name__ == '__main__':
    solve()