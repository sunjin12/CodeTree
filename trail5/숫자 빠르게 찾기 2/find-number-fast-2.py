import sys
from sortedcontainers import SortedSet

def solve():
    input = sys.stdin.readline

    N, M = map(int, input().split())
    
    # SortedSet 생성 (중복 제거 및 자동 정렬)
    s = SortedSet(map(int, input().split()))

    for _ in range(M):
        x = int(input())
        
        # x 이상인 원소의 첫 번째 인덱스
        idx = s.bisect_left(x)

        if idx < len(s):
            print(s[idx])
        else:
            print(-1)

if __name__ == '__main__':
    solve()