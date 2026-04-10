n = int(input())
lines = []
max_lines = 0
cur_lines = []

for _ in range(n):
    a, b = map(int, input().split())
    lines.append((a, b))

# 겹치는지 체크
def check_overlap():
    linechecker = [0] * 1001

    for line in cur_lines:
        a, b = line
        for i in range(a, b+1):
            linechecker[i] += 1
    
    if any(p >= 2 for p in linechecker):
        return True
    else:
        return False

# 선분 선택
def pick_line(i):
    global max_lines
    if i == n:
        if not check_overlap():
            max_lines = max(max_lines, len(cur_lines))
        return
    
    # i번째 선분을 넣는 경우X
    cur_lines.append(lines[i])
    pick_line(i+1)
    cur_lines.pop()

    # i번째 선분을 안 넣는 경우
    pick_line(i+1)

pick_line(0)

print(max_lines)
