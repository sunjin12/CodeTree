import sys
import heapq

def solve():
    input = sys.stdin.readline

    # N: 숫자의 개수
    N = int(input())

    # N개의 숫자를 입력받아 음수로 변환하여 최대 힙 구성
    numbers = list(map(int, input().split()))
    max_heap = [-x for x in numbers]
    heapq.heapify(max_heap)

    # 힙에 원소가 2개 이상 남아있을 때까지 반복
    while len(max_heap) >= 2:
        # 가장 큰 수 2개 꺼내기 (음수 상태이므로 -를 붙여 양수로 복원)
        first = -heapq.heappop(max_heap)
        second = -heapq.heappop(max_heap)

        # 차이 계산
        diff = first - second

        # 두 수가 같지 않다면 차이값을 다시 힙에 넣기
        if diff > 0:
            heapq.heappush(max_heap, -diff)

    # 최종 결과 출력
    if max_heap:
        print(-max_heap[0])
    else:
        print(-1)

if __name__ == '__main__':
    solve()