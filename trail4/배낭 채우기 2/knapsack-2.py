import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    N = int(data[0]) # 보석의 종류 수
    M = int(data[1]) # 배낭의 최대 무게
    
    # dp[j]: 정확히 j 무게를 채웠을 때의 최대 가치
    # (만약 'M 이하'의 최대 가치라면 0으로 초기화해도 되지만, 
    # '정확히 M'을 채우는 문제일 수 있으므로 안전하게 -1로 가겠습니다.)
    dp = [-1] * (M + 1)
    dp[0] = 0 # 0 무게는 가치 0으로 가능
    
    idx = 2
    for _ in range(N):
        w = int(data[idx])      # 보석의 무게
        p = int(data[idx+1])    # 보석의 가격
        idx += 2
        
        # ★★★ 핵심: 여러 개 선택 가능하므로 '정방향'으로 진행합니다.
        for j in range(w, M + 1):
            if dp[j - w] != -1:
                dp[j] = max(dp[j], dp[j - w] + p)
                
    # 만약 'M 이하'의 최대 가치를 묻는 문제라면 dp 배열 전체에서 max를 찾아야 하고,
    # '정확히 M'을 채우는 문제라면 dp[M]을 출력하면 됩니다.
    # 코드트리 배낭문제2가 'M 이하' 기준이라면 아래 주석을 해제하세요.
    print(max(dp))
    
if __name__ == '__main__':
    solve()