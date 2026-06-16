n = int(input())
arr = list(map(int, input().split()))

# 이제 기존 LIS 코드와 똑같이 진행합니다.
dp = [1] * n

for i in range(n):
    for j in range(i):
        if arr[j] > arr[i]: 
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))