n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]
ans = []
dist = int(1e9)

def cal_combination():
    global dist

    max_dist = 0
    for i in range(m):
        x1, y1 = ans[i]
        for j in range(i+1, m):
            x2, y2 = ans[j]
            cur_dist = (x1-x2)**2 + (y1-y2)**2
            if max_dist < cur_dist:
                max_dist = cur_dist
    
    dist = min(dist, max_dist)
             
        

def find_combination(curr_num, cnt):
    # m개를 모두 뽑았을 때 출력하고 종료
    if cnt == m:
        cal_combination()
        return

    for i in range(curr_num, n):
        ans.append(points[i])          # i번째 point 추가
        find_combination(i + 1, cnt + 1)  # 중복 방지 재귀
        ans.pop()              # 다시 되돌림 (백트래킹)

# 1부터 시작, 현재 0개 뽑음
find_combination(0, 0)

print(dist)