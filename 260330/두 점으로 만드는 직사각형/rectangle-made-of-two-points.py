x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

left = min(x1, a1)
right = max(x2, a2)
bottom = min(y1, b1)
top = max(y2, b2)

area = (top - bottom) * (right - left)

print(area)

