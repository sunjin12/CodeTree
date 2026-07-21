import sys

def solve():
    input = sys.stdin.readline

    # n: 첫 번째 수열 A의 크기
    n = int(input())
    # 수열 A를 set 구조로 바로 입력받아 탐색 속도 O(1) 확보
    set_a = set(map(int, input().split()))

    # m: 두 번째 수열 B의 크기
    m = int(input())
    # 수열 B 입력
    arr_b = list(map(int, input().split()))

    # 수열 B의 각 원소가 set_a에 존재하는지 확인
    for x in arr_b:
        if x in set_a:
            print(1)
        else:
            print(0)

if __name__ == '__main__':
    solve()