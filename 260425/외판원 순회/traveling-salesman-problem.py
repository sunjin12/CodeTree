import sys

# 입력 속도 향상
input = sys.stdin.readline

n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

# 시작점(0번)은 이미 방문한 것으로 간주
visited = [False] * n
min_value = int(1e9)

def traverse(cur, count, current_cost):
    global min_value

    # 1. 가지치기: 현재 비용이 이미 발견한 최솟값보다 크면 더 볼 필요 없음
    if current_cost >= min_value:
        return

    # 2. 종료 조건: 모든 도시를 방문했을 때
    if count == n:
        # 마지막 도시에서 시작점(0)으로 돌아가는 길이 있는지 확인
        if A[cur][0] != 0:
            min_value = min(min_value, current_cost + A[cur][0])
        return

    for i in range(n):
        # 방문하지 않았고, 길이 연결되어 있는 경우
        if not visited[i] and A[cur][i] != 0:
            visited[i] = True
            traverse(i, count + 1, current_cost + A[cur][i])
            visited[i] = False

# 0번 노드부터 시작 (방문 처리 필수)
visited[0] = True
traverse(0, 1, 0)

print(min_value)