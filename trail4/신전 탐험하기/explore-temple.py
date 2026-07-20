import sys

def solve():
    # input 속도 향상
    input = sys.stdin.readline

    # N: 신전의 층수
    N = int(input())

    # 층별 보물의 수 입력 (1층부터 N층까지)
    arr = [list(map(int, input().split())) for _ in range(N)]

    # dp[i][j] : i번째 층에서 j번째 방을 골랐을 때 보물 수의 최댓값
    dp = [[0] * 3 for _ in range(N)]

    # 1층 초기화 (index 0)
    dp[0][0] = arr[0][0]
    dp[0][1] = arr[0][1]
    dp[0][2] = arr[0][2]

    # 2층부터 N층까지 DP 진행
    for i in range(1, N):
        # 0번(왼쪽) 방 선택시 -> 이전 층에서 1번(가운데) 또는 2번(오른쪽) 선택 가능
        dp[i][0] = arr[i][0] + max(dp[i - 1][1], dp[i - 1][2])

        # 1번(가운데) 방 선택시 -> 이전 층에서 0번(왼쪽) 또는 2번(오른쪽) 선택 가능
        dp[i][1] = arr[i][1] + max(dp[i - 1][0], dp[i - 1][2])

        # 2번(오른쪽) 방 선택시 -> 이전 층에서 0번(왼쪽) 또는 1번(가운데) 선택 가능
        dp[i][2] = arr[i][2] + max(dp[i - 1][0], dp[i - 1][1])

    # N층(마지막 층)까지 올라왔을 때 세 방 중 최댓값 출력
    print(max(dp[N - 1]))

if __name__ == '__main__':
    solve()