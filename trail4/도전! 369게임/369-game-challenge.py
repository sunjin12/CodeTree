import sys

def solve():
    # 입력 처리
    input = sys.stdin.read
    token = input().strip()
    if not token:
        return
    
    N_str = token
    length = len(N_str)
    MOD = 10**9 + 7
    
    # 1. 입력 N을 정수화하되 큰 수이므로 자릿수 마다 % MOD 연산 적용하여 N_mod 계산
    N_mod = 0
    for char in N_str:
        N_mod = (N_mod * 10 + int(char)) % MOD

    # 2. DP 테이블 정의 및 채우기
    # DP[r][i] : 3, 6, 9를 쓰지 않고 i자리를 자유롭게 채웠을 때, 자릿수 합 % 3 == r 인 경우의 수
    # (선행 0이 오는 경우까지 모두 포함하는 표준 자릿수 DP 테이블)
    dp = [[0] * (length + 1) for _ in range(3)]
    dp[0][0] = 1 # 0자리일 때 합 0 (나머지 0)인 경우 1가지
    
    # 각 나머지를 가진 허용 숫자 개수: 0={0}(1개), 1={1,4,7}(3개), 2={2,5,8}(3개)
    for i in range(1, length + 1):
        for r in range(3):
            # 이전 자리 합의 나머지 r0에 허용 숫자(나머지 d_rem)를 더해 r을 만드는 경우의 수
            dp[r][i] = (dp[r][i] + dp[r][i-1] * 1) % MOD # 나머지 0짜리 (0)를 붙이는 경우
            dp[r][i] = (dp[r][i] + dp[(r-1)%3][i-1] * 3) % MOD # 나머지 1짜리 (1,4,7)를 붙이는 경우
            dp[r][i] = (dp[r][i] + dp[(r-2)%3][i-1] * 3) % MOD # 나머지 2짜리 (2,5,8)를 붙이는 경우

    # 3. N에 3, 6, 9가 있는 경우 그리디하게 변환하여 '박수가 절대 나오지 않는 상한선'으로 수정
    X = list(map(int, N_str))
    for i in range(length):
        if X[i] in (3, 6, 9):
            X[i] -= 1
            for j in range(i + 1, length):
                X[j] = 8
            break

    # 4. 변환된 수 X 이하의 자연수 중 '박수를 치지 않는 수'의 개수 구하기
    clean_count = 0
    prefix_sum = 0
    
    for i in range(length):
        limit = X[i]
        for d in range(limit):
            # 3, 6, 9는 건너뛰기
            if d in (3, 6, 9):
                continue
            
            # 맨 첫 자리에 0이 오는 것은 제외 (0보다 큰 자연수만을 세어야 하므로)
            if i == 0 and d == 0:
                continue
                
            # d를 선택했을 때의 현재 자릿수까지의 합의 나머지
            current_rem = (prefix_sum + d) % 3
            
            # 남은 뒷자리를 채워 최종 합이 3의 배수가 아니도록 (나머지가 0이 아니도록) 구성하는 경우의 수
            # 즉, (current_rem + 뒤_rem) % 3이 1 또는 2인 경우의 수
            rem_len = length - 1 - i
            clean_count = (clean_count + dp[(1 - current_rem) % 3][rem_len]) % MOD
            clean_count = (clean_count + dp[(2 - current_rem) % 3][rem_len]) % MOD
            
        prefix_sum = (prefix_sum + limit) % 3

    # N 자기 자신(변환된 X)도 조건에 부합하는지 검사
    if prefix_sum != 0:
        clean_count = (clean_count + 1) % MOD

    # 5. 자릿수가 N보다 작은 모든 수(1자리 ~ length-1자리)에 대해 '박수 안 치는 수' 누적 계산
    # (선행 0이 없는 유효한 자연수들만 구하므로 맨 앞자리는 1,2,4,5,7,8 중 하나로 시작해야 합니다.)
    for l in range(1, length):
        # 첫 자리가 1, 4, 7 (나머지 1인 수 3가지)인 경우
        clean_count = (clean_count + 3 * dp[(1 - 1) % 3][l - 1]) % MOD
        clean_count = (clean_count + 3 * dp[(2 - 1) % 3][l - 1]) % MOD
        # 첫 자리가 2, 5, 8 (나머지 2인 수 3가지)인 경우
        clean_count = (clean_count + 3 * dp[(1 - 2) % 3][l - 1]) % MOD
        clean_count = (clean_count + 3 * dp[(2 - 2) % 3][l - 1]) % MOD

    # 6. 전체 값 N_mod에서 박수를 치지 않는 수의 개수를 빼서 답을 도출
    ans = (N_mod - clean_count + MOD) % MOD
    print(ans)

if __name__ == "__main__":
    solve()