n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
visited = [False] * (n + 1)
nums = 0

# 인접 리스트 생성
graph = [[] for _ in range(n + 1)]
for edge in edges:
    a, b = edge
    graph[a].append(b)
    graph[b].append(a)


# DFS
def dfs(node):
    global nums

    for cur in graph[node]:
        if not visited[cur]:
            nums += 1
            visited[cur] = True
            dfs(cur)
    
visited[1] = True
dfs(1)

print(nums)


