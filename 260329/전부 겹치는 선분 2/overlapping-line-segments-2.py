n = int(input())
lines = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 두 라인 겹치는지 체크하는 함수
def is_intersect(x1, x2, x3, x4):
    return not (x2 < x3 or x4 < x1)

# for n 돌면서 i번째 선분은 제외
for i in range(n):
    is_valid = True
    for j in range(n):
        if j == i:
            continue
        x1, x2 = lines[j]
        
        for k in range(j+1, n):
            if k == i:
                continue
            x3, x4 = lines[k]
            # 나머지 선분끼리 겹치는지 체크 
            if not is_intersect(x1, x2, x3, x4):
                is_valid = False

    if is_valid:
        print("Yes")
        break
else:
    print("No")
    
        
