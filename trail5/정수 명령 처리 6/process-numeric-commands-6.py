import sys
import heapq

def solve():
    input = sys.stdin.readline

    # N: 명령의 개수
    N = int(input())

    # 최대 힙으로 사용할 리스트
    max_heap = []

    for _ in range(N):
        command = input().split()
        op = command[0]

        if op == "push":
            x = int(command[1])
            # 파이썬 heapq는 최소 힙이므로 음수로 변환하여 저장
            heapq.heappush(max_heap, -x)

        elif op == "pop":
            # 가장 큰 값 제거 후 부호를 반전시켜 출력
            val = heapq.heappop(max_heap)
            print(-val)

        elif op == "size":
            print(len(max_heap))

        elif op == "empty":
            if not max_heap:
                print(1)
            else:
                print(0)

        elif op == "top":
            # 가장 큰 값 출력 (삭제하지 않음)
            print(-max_heap[0])

if __name__ == '__main__':
    solve()