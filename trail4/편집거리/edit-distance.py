import sys

def solve():
    input = sys.stdin.readline

    # 두 문자열 입력 받기
    A = input().strip()
    B = input().strip()

    len_A = len(A)
    len_B = len(B)

    # dp[i][j]: A의 앞 i개 문자를 B의 앞 j개 문자로 변환하는 최소 연산 횟수
    dp = [[0] * (len_B + 1) for _ in range(len_A + 1)]

    # 1. 초기값 설정
    for i in range(len_A + 1):
        dp[i][0] = i  # A의 문자를 모두 삭제하는 연산
    for j in range(len_B + 1):
        dp[0][j] = j  # B의 문자를 모두 삽입하는 연산

    # 2. DP 테이블 채우기
    for i in range(1, len_A + 1):
        for j in range(1, len_B + 1):
            if A[i - 1] == B[j - 1]:
                # 문자가 같으면 이전 상태 비용 유지
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # 문자가 다르면 (수정, 삭제, 삽입) 중 최솟값 + 1
                dp[i][j] = min(
                    dp[i - 1][j - 1],  # 수정 (Replace)
                    dp[i - 1][j],      # 삭제 (Delete)
                    dp[i][j - 1]       # 삽입 (Insert)
                ) + 1

    # 3. 최종 최소 편집거리 출력
    print(dp[len_A][len_B])

if __name__ == '__main__':
    solve()