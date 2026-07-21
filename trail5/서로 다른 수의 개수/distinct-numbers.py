import sys

def solve():
    input = sys.stdin.readline

    # n: 숫자의 개수
    n = int(input())

    # 입력받은 숫자를 바로 set으로 변환하여 중복 제거
    numbers = set(map(int, input().split()))

    # 서로 다른 숫자의 개수(set의 크기) 출력
    print(len(numbers))

if __name__ == '__main__':
    solve()