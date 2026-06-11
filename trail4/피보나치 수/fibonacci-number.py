import sys

def get_fibonacci(n):
    # n이 1이거나 2일 때는 무조건 1을 반환
    if n <= 2:
        return 1
    
    # n번째 항까지 저장할 리스트 초기화 (인덱스를 n과 맞추기 위해 n+1 크기로 생성)
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 1
    
    # 3번째 항부터 n번째 항까지 앞의 두 항을 더해가며 채우기
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        
    return dp[n]

# 입력 받기
n = int(sys.stdin.readline())
print(get_fibonacci(n))