import sys
from sortedcontainers import SortedDict

def solve():
    input = sys.stdin.readline

    n = int(input())
    numbers = list(map(int, input().split()))

    # Key 기준 자동 정렬되는 SortedDict
    first_pos = SortedDict()

    for idx, num in enumerate(numbers, start=1):
        if num not in first_pos:
            first_pos[num] = idx

    # 이미 Key 기준 오름차순 정렬되어 있으므로 그대로 출력
    for num, pos in first_pos.items():
        print(f"{num} {pos}")

if __name__ == '__main__':
    solve()