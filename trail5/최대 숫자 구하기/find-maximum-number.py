import sys
from sortedcontainers import SortedSet

def solve():
    input = sys.stdin.readline

    # N: 초기에 들어있는 1~N까지의 자연수, M: 제거 연산의 개수
    N, M = map(int, input().split())

    # 1부터 N까지의 숫자를 담은 SortedSet 생성
    s = SortedSet(range(1, M + 1))

    # M개의 제거 명령 처리
    queries = list(map(int, input().split()))

    for x in queries:
        # 지정된 숫자 x 제거 (O(log N))
        s.discard(x)

        # 현재 남아있는 가장 큰 숫자 출력 (O(1))
        # SortedSet의 맨 마지막 원소가 항상 최댓값
        print(s[-1])

if __name__ == '__main__':
    solve()