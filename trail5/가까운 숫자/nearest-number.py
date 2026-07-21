import sys
from sortedcontainers import SortedSet

def solve():
    input = sys.stdin.readline

    # n: 추가될 점의 개수
    n = int(input())
    queries = list(map(int, input().split()))

    # 0 위치에 점이 하나 존재하는 상태로 시작
    s = SortedSet([0])

    # 현재 인접한 두 점 사이의 최소 거리 (초기값은 충분히 큰 값)
    min_dist = float('inf')

    for x in queries:
        # x를 집합에 추가하기 전, x보다 크거나 작은 위치 탐색
        idx = s.bisect_left(x)

        # x보다 작으면서 가장 가까운 점 (왼쪽 점)
        prev_pt = s[idx - 1]
        min_dist = min(min_dist, x - prev_pt)

        # x보다 크면서 가장 가까운 점 (오른쪽 점)이 존재하는 경우
        if idx < len(s):
            next_pt = s[idx]
            min_dist = min(min_dist, next_pt - x)

        # 점 x 추가
        s.add(x)

        # 현재까지의 최소 거리 출력
        print(min_dist)

if __name__ == '__main__':
    solve()