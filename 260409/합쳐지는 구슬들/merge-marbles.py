n, m, t = map(int, input().split())

balls = []

# 입력받을 때 1-based index를 0-based index로 맞추기 위해 1을 빼줍니다.
# 구슬의 번호(ID)는 입력 순서대로 1번부터 부여합니다.
for i in range(1, m + 1):
    ri, ci, di, wi = input().split()
    balls.append((i, int(ri) - 1, int(ci) - 1, di, int(wi)))

def is_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 이동 방향과 반대 방향을 쉽게 찾기 위한 딕셔너리
dirs = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}
opp_dirs = {'U': 'D', 'D': 'U', 'R': 'L', 'L': 'R'}

def sim(m, balls):
    # 2차원 배열 대신 딕셔너리를 사용하여 위치(좌표)별 구슬을 관리합니다.
    next_pos = {}

    # 1. 구슬 다음 위치 계산
    for i in range(m):
        num, x, y, d, w = balls[i]
        dx, dy = dirs[d]
        nx, ny = x + dx, y + dy
        
        # 격자를 벗어나는 경우 (벽에 부딪힘)
        # 위치는 이동하지 않고 제자리에 머물며 방향만 반대로 바꿉니다.
        if not is_range(nx, ny):
            nx, ny = x, y
            d = opp_dirs[d]
        
        # 딕셔너리에 해당 좌표가 없으면 빈 리스트 생성
        if (nx, ny) not in next_pos:
            next_pos[(nx, ny)] = []
            
        # 해당 위치에 구슬 추가
        next_pos[(nx, ny)].append((num, nx, ny, d, w))
        
    # 2. 겹친 구슬 합치기 및 다음 구슬 위치 기록
    new_balls = []
    
    for (x, y), ball_list in next_pos.items():
        if len(ball_list) == 1:
            # 겹치지 않은 구슬은 그대로 추가
            new_balls.append(ball_list[0])
        else:
            # 여러 구슬이 겹친 경우 합치기 로직
            total_weight = sum(b[4] for b in ball_list) # 모든 구슬의 무게 합산
            
            # 방향은 겹친 구슬 중 '가장 번호(num)가 큰 구슬'의 방향을 따름
            max_ball = max(ball_list, key=lambda b: b[0])
            
            # 합쳐진 새로운 구슬 생성 (가장 큰 번호 유지, 위치, 방향, 합산된 무게)
            new_balls.append((max_ball[0], x, y, max_ball[3], total_weight))
            
    return len(new_balls), new_balls

# t초 시뮬레이션
for _ in range(t):
    m, balls = sim(m, balls)

# 남아있는 구슬 중 가장 무거운 구슬의 무게 찾기
max_w = 0
for ball in balls:
    max_w = max(max_w, ball[4])

print(m, max_w)