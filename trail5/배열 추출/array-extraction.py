import sys
import heapq

def solve():
    input = sys.stdin.readline

    # n: 연산의 개수
    n = int(input())

    # 최대 힙 리스트
    max_heap = []

    for _ in range(n):
        x = int(input())

        if x == 0:
            # 힙이 비어있으면 0 출력
            if not max_heap:
                print(0)
            else:
                # 가장 큰 값 출력 (음수로 들어갔으므로 다시 -를 붙여 복원)
                print(-heapq.heappop(max_heap))
        else:
            # 자연수인 경우 음수로 변환하여 힙에 추가
            heapq.heappush(max_heap, -x)

if __name__ == '__main__':
    solve()