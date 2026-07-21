import sys
from sortedcontainers import SortedDict

def solve():
    input = sys.stdin.readline

    # n: 명령어의 개수
    n = int(input())

    # Key가 자동 정렬되는 SortedDict 생성
    treemap = SortedDict()

    for _ in range(n):
        command = input().split()
        op = command[0]

        if op == "add":
            k, v = int(command[1]), int(command[2])
            treemap[k] = v  # O(log N)으로 정렬 상태 유지하며 삽입/갱신

        elif op == "remove":
            k = int(command[1])
            if k in treemap:
                del treemap[k]  # O(log N)으로 삭제

        elif op == "find":
            k = int(command[1])
            if k in treemap:
                print(treemap[k])
            else:
                print("None")

        elif op == "print_list":
            if not treemap:
                print("None")
            else:
                # 이미 Key 기준 오름차순 정렬되어 있으므로 values()를 그대로 가져옴
                values = [str(v) for v in treemap.values()]
                print(" ".join(values))

if __name__ == '__main__':
    solve()