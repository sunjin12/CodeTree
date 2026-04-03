n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

max_coins = 0

def pick_coins(x, y):
    coins = 0
    for i in range(x, x+3):
        for j in range(y, y+3):
            coins += grid[i][j]
    return coins


for i in range(n-2):
    for j in range(n-2):
        max_coins = max(max_coins, pick_coins(i, j))

print(max_coins)

