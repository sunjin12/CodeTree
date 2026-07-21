import sys

def solve():
    input = sys.stdin.readline

    # 두 문자열 입력 받기
    A = input().strip()
    B = input().strip()

    len_A = len(A)
    len_B = len(B)

    # dp[i][j] : A의 i번째 문자와 B의 j번째 문자까지 비교했을 때의 LCS 길이
    # 인덱스 처리를 편하게 하기 위해 (len_A + 1) x (len_B + 1) 크기 배열 생성
    dp = [[0] * (len_B + 1) for _ in range(len_A + 1)]

    # DP 테이블 채우기
    for i in range(1, len_A + 1):
        for j in range(1, len_B + 1):
            if A[i - 1] == B[j - 1]:
                # 두 문자가 같으면 빗각(이전 상태)에서 +1
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # 두 문자가 다르면 위쪽이나 왼쪽 값 중 최댓값 선택
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # 최종 결과 출력 (두 문자열 전체를 비교한 LCS 길이)
    print(dp[len_A][len_B])

if __name__ == '__main__':
    solve()