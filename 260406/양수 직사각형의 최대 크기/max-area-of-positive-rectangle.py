n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

max_rec = 0

# 정점 기준으로 오른/아래 직사각형 최댓값 리턴
def rec(x, y):
    m_rec = 0
    for i in range(x, n):
        rec = 0
        max_col = m
        for j in range(x, i+1):
            for k in range(y, m):
                if grid[j][k] < 0:
                    max_col = min(max_col, k)
        rec = (i - x + 1) * (max_col - y)

        m_rec = max(m_rec, rec)
    
    return m_rec

# n * m 순회
for i in range(n):
    for j in range(m):
        max_rec = max(max_rec, rec(i, j))

if max_rec == 0:
    print(-1)
else:
    print(max_rec)