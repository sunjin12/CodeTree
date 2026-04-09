n, m, t = map(int, input().split())

# Create n x n grid
a = [list(map(int, input().split())) for _ in range(n)]

# Get m marble positions
marbles = [tuple(map(int, input().split())) for _ in range(m)]
r = [pos[0] - 1 for pos in marbles]
c = [pos[1] - 1 for pos in marbles]

def is_range(x, y):
    return 0 <= x < n and 0 <= y < n

def sim(m, r, c):
    next_pos = [[0] * n for _ in range(n)]
    dxys = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 구슬 다음 위치 계산
    for i in range(m):
        x, y = r[i], c[i]
        c_max = a[x][y]
        mx, my = x, y
        for dx, dy in dxys:
            nx, ny = x + dx, y + dy
            if is_range(nx, ny) and a[nx][ny] > c_max:
                mx, my = nx, ny
        
        next_pos[mx][my] += 1
    
    # 겹친 구슬 제거
    for i in range(n):
        for j in range(n):
            if next_pos[i][j] > 1:
                next_pos[i][j] = 0

    # 다음 구슬 위치 기록
    r, c, m = [], [], 0
    for i in range(n):
        for j in range(n):
            if next_pos[i][j]:
                r.append(i)
                c.append(j)
                m += 1
    
    return m, r, c



# t초 시뮬레이션
for _ in range(t):
    m, r, c = sim(m, r, c)

print(m)




