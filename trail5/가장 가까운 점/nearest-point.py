import sys
import heapq

def solve():
    input = sys.stdin.readline

    # N: 점의 개수, M: 반복 횟수
    N, M = map(int, input().split())

    min_heap = []

    # N개의 점 입력받아 (x+y, x, y) 형태 튜플로 힙에 저장
    for _ in range(N):
        x, y = map(int, input().split())
        heapq.heappush(min_heap, (x + y, x, y))

    # M번 반복하며 가장 가까운 점 좌표 (x+2, y+2)로 갱신
    for _ in range(M):
        _, x, y = heapq.heappop(min_heap)
        nx, ny = x + 2, y + 2
        heapq.heappush(min_heap, (nx + ny, nx, ny))

    # 최종적으로 가장 우선순위가 높은(가장 가까운) 점의 x, y 좌표 출력
    _, ans_x, ans_y = heapq.heappop(min_heap)
    print(f"{ans_x} {ans_y}")

if __name__ == '__main__':
    solve()