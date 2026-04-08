from enum import Enum

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# UP(0), DOWN(1), LEFT(2), RIGHT(3)
dxys = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class Dir(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

def is_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 방향전환 시뮬레이션
def sim(x, y, d):
    cnt = 1  # 격자에 처음 진입하는 데 걸리는 시간 1초
    
    while is_range(x, y):
        # 1번 거울 (/) : 상<->우, 하<->좌
        if grid[x][y] == 1:
            if d == Dir.UP: d = Dir.RIGHT
            elif d == Dir.LEFT: d = Dir.DOWN
            elif d == Dir.DOWN: d = Dir.LEFT
            else: d = Dir.UP
            
        # 2번 거울 (\) : 상<->좌, 하<->우
        elif grid[x][y] == 2:
            if d == Dir.UP: d = Dir.LEFT
            elif d == Dir.LEFT: d = Dir.UP
            elif d == Dir.DOWN: d = Dir.RIGHT
            else: d = Dir.DOWN
            
        # grid[x][y] == 0 (빈 칸)인 경우 방향 전환 로직을 건너뛰고 직진합니다.
        
        # d.value를 사용하여 Enum에서 정수값을 추출
        x, y = x + dxys[d.value][0], y + dxys[d.value][1]
        cnt += 1  # 이동 완료 후 1초 증가
    
    return cnt

max_time = 0

# 윗면에서 아래로 진입 / 아랫면에서 위로 진입
for j in range(n):
    max_time = max(max_time, sim(0, j, Dir.DOWN), sim(n-1, j, Dir.UP))

# 왼면에서 오른쪽으로 진입 / 오른면에서 왼쪽으로 진입
for i in range(n):
    max_time = max(max_time, sim(i, 0, Dir.RIGHT), sim(i, n-1, Dir.LEFT))

print(max_time)