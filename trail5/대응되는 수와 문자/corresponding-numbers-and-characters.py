import sys

def solve():
    input = sys.stdin.readline

    # N: 단어의 개수, M: 질의의 개수
    N, M = map(int, input().split())

    # 1. 1-based index를 위한 리스트 (숫자 -> 문자)
    num_to_str = [""] * (N + 1)
    
    # 2. 딕셔너리 (문자 -> 숫자)
    str_to_num = {}

    # N개의 문자열 입력 받기
    for i in range(1, N + 1):
        s = input().strip()
        num_to_str[i] = s
        str_to_num[s] = i

    # M개의 질의 처리
    for _ in range(M):
        q = input().strip()

        # 입력이 숫자인 경우 -> 해당 번호의 문자열 출력
        if q.isdigit():
            idx = int(q)
            print(num_to_str[idx])
        # 입력이 문자열인 경우 -> 해당 문자열의 번호 출력
        else:
            print(str_to_num[q])

if __name__ == '__main__':
    solve()