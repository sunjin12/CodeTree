n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

# visited 배열
visited = [False] * n

min_value = int(1e9)

# traverse 함수: 입력 - (현재 노드, 지금까지 방문 노드 수, 지금까지 비용)
def traverse(cur, nums, values):
    global min_value
    
    if nums == n and cur == 0:
        min_value = min(min_value, values)
        return

    for i in range(n):
        if A[cur][i] != 0 and visited[i] is False:
            visited[i] = True
            traverse(i, nums+1, values+A[cur][i])
            visited[i] = False

# 최소 비용 출력
traverse(0, 0, 0)

print(min_value)