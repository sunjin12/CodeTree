import sys
from sortedcontainers import SortedSet

def solve():
    input = sys.stdin.readline

    # n: 명령어의 개수
    n = int(input())

    # 원소가 자동으로 정렬되는 SortedSet 생성
    s = SortedSet()

    for _ in range(n):
        command = input().split()
        op = command[0]

        if op == "add":
            x = int(command[1])
            s.add(x)

        elif op == "remove":
            x = int(command[1])
            s.discard(x)  # 원소가 없어도 에러 없이 안전하게 제거

        elif op == "find":
            x = int(command[1])
            if x in s:
                print("true")
            else:
                print("false")

        elif op == "lower_bound":
            x = int(command[1])
            # x 이상인 원소의 첫 번째 위치 찾기
            idx = s.bisect_left(x)
            if idx < len(s):
                print(s[idx])
            else:
                print("None")

        elif op == "upper_bound":
            x = int(command[1])
            # x 초과인 원소의 첫 번째 위치 찾기
            idx = s.bisect_right(x)
            if idx < len(s):
                print(s[idx])
            else:
                print("None")

        elif op == "largest":
            if s:
                print(s[-1])  # 정렬된 상태이므로 맨 뒤가 최댓값
            else:
                print("None")

        elif op == "smallest":
            if s:
                print(s[0])   # 정렬된 상태이므로 맨 앞이 최솟값
            else:
                print("None")

if __name__ == '__main__':
    solve()