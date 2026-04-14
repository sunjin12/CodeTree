import sys

# n: 전체 숫자의 범위 (1~n), m: 뽑을 개수
n, m = map(int, sys.stdin.readline().split())
ans = []

def print_combination():
    for val in ans:
        print(val, end=" ")
    print()

def find_combination(curr_num, cnt):
    # m개를 모두 뽑았을 때 출력하고 종료
    if cnt == m:
        print_combination()
        return

    # curr_num부터 n까지의 숫자를 후보로 확인
    for i in range(curr_num, n + 1):
        ans.append(i)          # 숫자를 뽑음
        find_combination(i + 1, cnt + 1)  # 다음 숫자는 현재보다 큰 숫자로 (중복 방지)
        ans.pop()              # 다시 되돌림 (백트래킹)

# 1부터 시작, 현재 0개 뽑음
find_combination(1, 0)