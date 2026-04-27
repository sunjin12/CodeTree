import sys

# 입력 속도 향상
input = sys.stdin.readline

# n: 격자의 크기
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n
# 우리가 찾고자 하는 것은 '최솟값들 중 최대'이므로, 결과값은 아주 작은 수로 시작합니다.
ans = 0

def backtrack(row, current_min):
    global ans

    # 모든 행을 다 확인했다면 (n개의 숫자를 다 골랐다면)
    if row == n:
        # 지금까지 고른 숫자들 중 최솟값(current_min)이 
        # 기존에 알고 있던 최대 최솟값보다 크다면 갱신
        ans = max(ans, current_min)
        return

    for col in range(n):
        if not visited[col]:
            visited[col] = True
            
            # 다음 행으로 이동하며 지금까지의 최솟값을 갱신하여 전달
            # 초기값(row=0)일 때는 현재 칸의 값을 그대로 전달
            next_min = min(current_min, grid[row][col])
            
            # 가지치기(Optimization): 
            # 만약 현재까지의 최솟값이 이미 발견한 정답(ans)보다 작거나 같다면 
            # 더 이상 탐색할 필요가 없습니다. (선택 사항)
            if next_min > ans:
                backtrack(row + 1, next_min)
            
            visited[col] = False

# 초기 최솟값은 아주 큰 값으로 시작하거나, 첫 번째 선택에서 처리되도록 설정합니다.
backtrack(0, float('inf'))
print(ans)