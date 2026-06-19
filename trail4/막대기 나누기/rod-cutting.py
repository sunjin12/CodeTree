import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    # N: 막대의 총 길이
    N = int(data[0])
    
    # 1부터 N까지의 각 길이별 가격 정보 (인덱스를 맞추기 위해 앞에 0 추가)
    # 입력 형식에 따라 대입 (예: 가격 정보가 N개 연속으로 들어오는 경우)
    prices = [0] + [int(x) for x in data[1:N+1]]
    
    # dp[j]: 길이가 j인 막대를 잘라 얻을 수 있는 최대 금액
    dp = [0] * (N + 1)
    
    # j: 만들고자 하는 막대의 목표 길이
    for j in range(1, N + 1):
        # i: 마지막으로 자를 조각의 길이
        for i in range(1, j + 1):
            dp[j] = max(dp[j], prices[i] + dp[j - i])
            
    # 총 길이 N일 때의 최대 이익 출력
    print(dp[N])

if __name__ == '__main__':
    solve()