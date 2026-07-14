import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    N = int(data[0])
    
    # 각 학생의 능력치 저장 (축구 능력, 야구 능력)
    students = []
    idx = 1
    for _ in range(N):
        s = int(data[idx])
        b = int(data[idx+1])
        students.append((s, b))
        idx += 2
        
    # 축구팀은 정확히 11명, 야구팀은 정확히 9명
    MAX_S = 11
    MAX_B = 9
    
    # dp[i][j] : 축구 i명, 야구 j명 뽑았을 때의 최댓값
    # 도달할 수 없는 상태는 무한히 작은 값(-float('inf'))으로 초기화
    dp = [[-float('inf')] * (MAX_B + 1) for _ in range(MAX_S + 1)]
    dp[0][0] = 0 # 아무도 안 뽑았을 때의 합은 0
    
    # 모든 학생을 한 명씩 확인
    for s_stat, b_stat in students:
        # 중복 선택 방지를 위해 뒤에서부터 역순으로 DP 테이블 갱신
        for i in range(MAX_S, -1, -1):
            for j in range(MAX_B, -1, -1):
                if dp[i][j] == -float('inf'):
                    continue
                
                # 선택지 1: 현재 학생을 축구팀에 배치하는 경우
                if i + 1 <= MAX_S:
                    dp[i+1][j] = max(dp[i+1][j], dp[i][j] + s_stat)
                    
                # 선택지 2: 현재 학생을 야구팀에 배치하는 경우
                if j + 1 <= MAX_B:
                    dp[i][j+1] = max(dp[i][j+1], dp[i][j] + b_stat)
                    
                # 선택지 3: 아무 팀에도 넣지 않는 경우는 dp[i][j] 유지되므로 코딩 생략
                
    # 정확히 축구 11명, 야구 9명을 채웠을 때의 최댓값 출력
    print(dp[MAX_S][MAX_B])

if __name__ == "__main__":
    solve()