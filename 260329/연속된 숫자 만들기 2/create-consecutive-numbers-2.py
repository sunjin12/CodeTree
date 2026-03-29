pos = list(map(int, input().split()))
pos.sort()
a, b, c = pos[0], pos[1], pos[2]

if a + 1 == b and b + 1 == c:
    print(0)
elif a + 1 == b or b + 1 == c or a + 2 == b or b + 2 == c:
    print(1)
else:
    print(2)

