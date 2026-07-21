import sys

def solve():
    input = sys.stdin.readline

    # N: 첫 번째 수열 A의 크기
    n = int(input())
    # 수열 A를 set 구조로 입력받아 중복 제거 및 O(1) 탐색 준비
    set_a = set(map(int, input().split()))

    # M: 두 번째 수열 B의 크기
    m = int(input())
    # 수열 B 입력
    arr_b = list(map(int, input().split()))

    # 수열 B의 각 원소가 set_a에 존재하는지 확인
    result = []
    for x in arr_b:
        if x in set_a:
            result.append("1")
        else:
            result.append("0")

    # 결과를 공백으로 구분하여 출력
    print(" ".join(result))

if __name__ == '__main__':
    solve()