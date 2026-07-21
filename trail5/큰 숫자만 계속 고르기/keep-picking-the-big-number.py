import sys
import heapq

def solve():
    input = sys.stdin.readline

    # N: 숫자의 개수, M: 반복 횟수
    N, M = map(int, input().split())

    # 숫자가 들어있는 리스트 입력 받기
    numbers = list(map(int, input().split()))

    # 파이썬 heapq는 최소 힙이므로 음수로 변환하여 최대 힙 구현
    max_heap = [-x for x in numbers]
    heapq.heapify(max_heap)

    # M번 동안 가장 큰 수 1씩 감소시키기
    for _ in range(M):
        # 가장 큰 수 꺼내기 (음수 상태이므로 abs 또는 - 붙여서 복원)
        max_val = -heapq.heappop(max_heap)
        
        # 1 감소시킨 후 다시 힙에 음수로 저장
        heapq.heappush(max_heap, -(max_val - 1))

    # 남아있는 모든 수의 합 계산
    # max_heap 내부의 값들이 음수이므로 -sum()을 통해 양수 합을 구함
    ans = -heapq.heappop(max_heap)
    print(ans)

if __name__ == '__main__':
    solve()