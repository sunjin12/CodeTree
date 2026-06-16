import sys

# 입력 받기
n = int(input())
arr = list(map(int, input().split()))

# 1. dp 테이블을 -1로 초기화 (도달할 수 없는 상태를 의미)
dp = [-1] * n

# 2. 시작점은 점프 0번으로 도달 가능하므로 0으로 설정
dp[0] = 0

# 3. DP 진행 (O(N^2))
for i in range(1, n):
    for j in range(i):
        # 조건 1: j번째 칸이 도달 가능한 칸이어야 하고
        # 조건 2: j번째 칸에서 점프해서 i번째 칸에 도달할 수 있어야 함
        if dp[j] != -1 and j + arr[j] >= i:
            # 기존 dp[i]와 j에서 점프해서 오는 경우(dp[j] + 1) 중 최댓값 선택
            dp[i] = max(dp[i], dp[j] + 1)

# 4. dp 배열에 저장된 값 중 최댓값이 "최대 점프 횟수"가 됩니다.
print(max(dp))