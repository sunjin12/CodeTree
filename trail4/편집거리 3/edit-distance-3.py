import sys

def solve():
    input = sys.stdin.readline

    # 두 문자열 입력
    A = input().strip()
    B = input().strip()

    len_A = len(A)
    len_B = len(B)

    # dp[i][j]: A의 앞 i개 문자를 B의 앞 j개 문자로 변환하는 최소 삽입/삭제 횟수
    dp = [[0] * (len_B + 1) for _ in range(len_A + 1)]

    # 초기값 설정
    # A의 문자를 B(빈 문자열)로 만들려면 i번 삭제해야 함
    for i in range(len_A + 1):
        dp[i][0] = i
    # 빈 문자열 A를 B의 j개 문자로 만들려면 j번 삽입해야 함
    for j in range(len_B + 1):
        dp[0][j] = j

    # DP 테이블 채우기
    for i in range(1, len_A + 1):
        for j in range(1, len_B + 1):
            if A[i - 1] == B[j - 1]:
                # 두 문자가 같으면 연산 필요 없음
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # 두 문자가 다르면 (삭제, 삽입) 중 최솟값 + 1
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1

    print(dp[len_A][len_B])

if __name__ == '__main__':
    solve()