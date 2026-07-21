import sys
from collections import Counter

def solve():
    input = sys.stdin.readline

    # n: 문자열의 개수
    n = int(input())

    # n개의 문자열을 입력받아 리스트로 저장
    words = [input().strip() for _ in range(n)]

    # 각 문자열의 빈도수를 세어주는 Counter 객체 생성
    counts = Counter(words)

    # 가장 많이 등장한 문자열의 횟수(values 중 최댓값) 출력
    print(max(counts.values()))

if __name__ == '__main__':
    solve()