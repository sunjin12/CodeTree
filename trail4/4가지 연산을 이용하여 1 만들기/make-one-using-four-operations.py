from collections import deque
import sys

input = sys.stdin.readline


def solve():
    n = int(input())

    # 1에서 시작해서 N까지 가므로, 탐색 범위를 N의 2배 혹은 최대값으로 제한합니다.
    # 대략 N의 2배를 넘는 연산은 비효율적이므로 MAX 범위를 설정합니다.
    MAX_VAL = max(n * 2, 10)
    visited = [-1] * (MAX_VAL + 1)

    # 1에서 출발
    queue = deque([1])
    visited[1] = 0

    while queue:
        curr = queue.popleft()

        # 목표 숫자 N에 도달하면 연산 횟수 반환
        if curr == n:
            print(visited[curr])
            return

        # 4가지 역연산 가능성 체크
        # 1. 1을 더하기 (원래 연산에서 1을 빼는 것에 대응)
        # 2. 1을 빼기 (원래 연산에서 1을 더하는 것에 대응)
        # 3. 2를 곱하기 (원래 연산에서 2로 나누는 것에 대응)
        # 4. 3을 곱하기 (원래 연산에서 3으로 나누는 것에 대응)
        next_states = [curr + 1, curr - 1, curr * 2, curr * 3]

        for nxt in next_states:
            # 유효한 범위 내에 있고, 아직 방문하지 않은 숫자인 경우
            if 1 <= nxt <= MAX_VAL and visited[nxt] == -1:
                visited[nxt] = visited[curr] + 1
                queue.append(nxt)


solve()