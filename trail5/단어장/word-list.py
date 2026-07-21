import sys
from sortedcontainers import SortedDict

def solve():
    input = sys.stdin.readline

    n = int(input())

    # Key가 자동으로 사전순 정렬되는 SortedDict
    word_counts = SortedDict()

    for _ in range(n):
        word = input().strip()
        word_counts[word] = word_counts.get(word, 0) + 1

    # 이미 사전순 정렬되어 있으므로 순서대로 출력
    for word, count in word_counts.items():
        print(f"{word} {count}")

if __name__ == '__main__':
    solve()