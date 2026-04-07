n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def is_range(x, y):
    return 0 <= x < n and 0 <= y < n

def check_pair(mat):
    cnt = 0
    # 위아래
    for i in range(n-1):
        for j in range(n):
            if mat[i][j] != -1 and mat[i][j] == mat[i+1][j]:
                cnt += 1

    # 양 옆
    for i in range(n):
        for j in range(n-1):
            if mat[i][j] != -1 and mat[i][j] == mat[i][j+1]:
                cnt += 1

    return cnt



def bomb(x, y, k):
    dxs, dys = [0, 0, -1, 1], [-1, 1, 0, 0]
    clone = [row[:] for row in grid]
    
    # 원본 grid에서 원점 + 4방향 k만큼 -1로 치환한 복제 배열 생성
    clone[x][y] = -1
    for l in range(1, k+1):
        for dx, dy in zip(dxs, dys):
            nx, ny = x + (dx * l), y + (dy * l)
            if is_range(nx, ny):
                clone[nx][ny] = -1  

    # 중력에 의해 떨어지기
    output = []
    for j in range(n):
        tmp = []
        for i in range(n-1, -1, -1):
            if clone[i][j] != -1:
                tmp.append(clone[i][j])
        
        while len(tmp) < n:
            tmp.append(-1)
        
        output.append(tmp)
    
    return output

max_pairs = 0

# n x n 순환
for i in range(n):
    for j in range(n):
        # 폭탄 터진 후 매트릭스
        k = grid[i][j] - 1
        after_bomb = bomb(i, j, k)

        # 숫자쌍 체크
        max_pairs = max(max_pairs, check_pair(after_bomb))

# 제일 큰 숫자쌍 갯수 출력
print(max_pairs)





