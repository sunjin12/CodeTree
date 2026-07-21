import sys
import heapq

def solve():
    input = sys.stdin.readline

    # N: 연산의 개수
    N = int(input())

    # 최소 힙 리스트
    min_heap = []

    for _ in range(N):
        x = int(input())

        if x == 0:
            # 힙이 비어있으면 0 출력
            if not min_heap:
                print(0)
            else:
                # 가장 작은 값 출력 후 제거
                print(heapq.heappop(min_heap))
        else:
            # 자연수 입력 시 힙에 추가
            heapq.heappush(min_heap, x)

if __name__ == '__main__':
    solve()