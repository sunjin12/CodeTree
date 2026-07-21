import sys
from sortedcontainers import SortedDict

def solve():
    input = sys.stdin.readline

    n = int(input())
    
    # 자동으로 Key가 사전순 정렬되는 SortedDict
    counts = SortedDict()

    for _ in range(n):
        word = input().strip()
        counts[word] = counts.get(word, 0) + 1

    # 이미 사전순으로 정렬되어 있으므로 그대로 순회
    for word, count in counts.items():
        ratio = (count / n) * 100
        print(f"{word} {ratio:.4f}")

if __name__ == '__main__':
    solve()