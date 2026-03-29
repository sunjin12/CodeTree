n = int(input())
pigeons = [-1] * 11
cnt = 0

for _ in range(n):
    pigeon, line = map(int, input().split())
    if pigeons[pigeon] == -1:
        pigeons[pigeon] = line
    elif pigeons[pigeon] == line:
        continue
    else:
        pigeons[pigeon] ^= 1
        cnt += 1

print(cnt)