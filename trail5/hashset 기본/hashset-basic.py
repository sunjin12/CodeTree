import sys

def solve():
    input = sys.stdin.readline

    # n: 명령어의 개수
    n = int(input())

    # 원소를 보관할 HashSet (파이썬 set)
    s = set()

    for _ in range(n):
        command = input().split()
        op = command[0]
        x = int(command[1])

        if op == "add":
            s.add(x)

        elif op == "remove":
            # KeyError 방지를 위해 discard 사용 (또는 x in s 확인 후 remove)
            s.discard(x)

        elif op == "find":
            if x in s:
                print("true")
            else:
                print("false")

if __name__ == '__main__':
    solve()