# N: 원소의 개수, arr: 수열 입력 예시
n = int(input())
arr = list(map(int, input().split()))

# 1. 모든 위치의 dp 값을 1로 초기화 (자기 자신만 포함하는 수열의 길이)
dp = [1] * n

# 2. LIS 로직 진행 (O(N^2))
for i in range(n):
    for j in range(i):
        # 앞에 있는 원소(j)가 현재 원소(i)보다 작은 경우
        if arr[j] < arr[i]:
            # 기존 dp[i]와 이전 dp[j]에 현재 원소를 추가한 값(dp[j] + 1) 중 큰 값으로 갱신
            dp[i] = max(dp[i], dp[j] + 1)

# 3. dp 배열의 최댓값이 전체 수열의 최장 증가 부분 수열의 길이가 됩니다.
print(max(dp))