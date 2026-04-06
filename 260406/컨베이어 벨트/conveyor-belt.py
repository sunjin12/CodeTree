from collections import deque

n, t = map(int, input().split())
uc = deque(list(map(int, input().split())))
dc = deque(list(map(int, input().split())))

for _ in range(t):
    uc.appendleft(dc.pop())
    dc.appendleft(uc.pop())

print(" ".join(map(str, uc)))
print(" ".join(map(str, dc)))
