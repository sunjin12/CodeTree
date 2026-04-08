n, r, c = map(int, input().split())
a = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        a[i][j] = row[j - 1]

def is_range(x, y):
    return 1 <= x <= n and 1 <= y <= n

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

is_changed = True
while is_changed:
    print(a[r][c], end=' ')
    for dr, dc in zip(dxs, dys):
        nr, nc = r + dr, c + dc
        if is_range(nr, nc) and a[nr][nc] > a[r][c]:
            r, c = nr, nc
            break
    else:
        is_changed = False


