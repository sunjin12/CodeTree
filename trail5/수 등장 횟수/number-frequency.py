import sys

def solve():
    input = sys.stdin.readline

    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    # 해시맵 생성 및 카운팅
    count_map = {}
    for num in numbers:
        count_map[num] = count_map.get(num, 0) + 1

    # 질의 처리
    queries = list(map(int, input().split()))
    result = [str(count_map.get(q, 0)) for q in queries]

    print(' '.join(result))

if __name__ == '__main__':
    solve()