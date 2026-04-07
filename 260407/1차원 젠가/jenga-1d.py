n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

s1, e1, s2, e2 = s1-1, e1-1, s2-1, e2-1

# 첫 번 쨰
tmp1 = []
for i in range(n):
    if s1 <= i <= e1:
        continue
    tmp1.append(blocks[i])

# 두 번 쨰
l = len(tmp1)
tmp2 = []
for i in range(l):
    if s2 <= i <= e2:
        continue
    tmp2.append(tmp1[i])

# 출력
print(len(tmp2))
for b in tmp2:
    print(b)