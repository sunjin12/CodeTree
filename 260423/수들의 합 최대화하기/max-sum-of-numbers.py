# n: 격자의 크기
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n
max_sum = 0

def backtrack(row, current_sum):
    global max_sum
    
    # 모든 행을 다 확인했다면 최댓값 갱신
    if row == n:
        max_sum = max(max_sum, current_sum)
        return

    for col in range(n):
        # 해당 열을 아직 선택하지 않았다면
        if not visited[col]:
            visited[col] = True  # 방문 표시
            backtrack(row + 1, current_sum + grid[row][col])
            visited[col] = False # 원상 복구 (Backtrack)

backtrack(0, 0)
print(max_sum)