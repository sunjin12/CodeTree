import sys
from bisect import bisect_left

def solve():
    input = sys.stdin.readline

    # N: 점의 개수, M: 질의의 개수
    N, M = map(int, input().split())

    # N개의 (x, y) 점들을 튜플로 입력받기
    points = []
    for _ in range(N):
        x, y = map(int, input().split())
        points.append((x, y))

    # (x, y) 기준 오름차순 정렬
    # (x 오름차순 -> x가 같으면 y 오름차순)
    points.sort()

    # M개의 질의 처리
    for _ in range(M):
        qx, qy = map(int, input().split())

        # (qx, qy) 이상인 첫 번째 점의 위치를 이진 탐색으로 찾기
        idx = bisect_left(points, (qx, qy))

        # 범위 내에 존재하는 경우 해당 점 출력
        if idx < N:
            print(f"{points[idx][0]} {points[idx][1]}")
        else:
            print("-1 -1")

if __name__ == '__main__':
    solve()