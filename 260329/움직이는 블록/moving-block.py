n = int(input())
blocks = [int(input()) for _ in range(n)]
total = sum(blocks)
avg = total // n
cnt = 0

for block in blocks:
    if block > avg:
        cnt += (block - avg)

print(cnt)