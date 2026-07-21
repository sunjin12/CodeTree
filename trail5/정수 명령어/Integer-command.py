import sys
from sortedcontainers import SortedSet

def solve():
    input = sys.stdin.readline

    # T: 테스트 케이스 수
    T = int(input())

    for _ in range(T):
        # k: 연산의 개수
        k = int(input())
        s = SortedSet()

        for _ in range(k):
            cmd, val = input().split()
            val = int(val)

            if cmd == 'I':
                s.add(val)
            elif cmd == 'D':
                if not s:
                    continue
                if val == 1:
                    # 최댓값 삭제 (맨 뒤 원소 제거)
                    s.pop(-1)
                elif val == -1:
                    # 최솟값 삭제 (맨 앞 원소 제거)
                    s.pop(0)

        # 결과 출력
        if not s:
            print("EMPTY")
        else:
            print(f"{s[-1]} {s[0]}")

if __name__ == '__main__':
    solve()