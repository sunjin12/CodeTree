n = int(input())
a = b = 0
cur_honor = 0
cnt = 0

def honor_state(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    return 0

for _ in range(n):
    c, s = input().split()
    s = int(s)

    if c == 'A':
        a += s
    else:
        b += s

    next_honor = honor_state(a, b)

    if cur_honor != next_honor:
        cur_honor = next_honor
        cnt += 1

print(cnt)
    
    


