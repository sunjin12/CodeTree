import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    n = int(data[0])
    
    # 선분 정보 입력 받기
    segments = []
    idx = 1
    for _ in range(n):
        x1 = int(data[idx])
        x2 = int(data[idx+1])
        segments.append((x1, x2))
        idx += 2
        
    # 1. 시작점 기준 오름차순 정렬
    segments.sort()
    
    # 2. dp 배열 초기화 (각 선분은 자기 자신만으로 최소 1개의 선분을 가짐)
    dp = [1] * n
    
    # 3. DP 수행 (O(N^2))
    for i in range(1, n):
        curr_start, curr_end = segments[i]
        
        for j in range(i):
            prev_start, prev_end = segments[j]
            
            # 이전 선분의 끝점이 현재 선분의 시작점보다 작으면 겹치지 않음
            if prev_end < curr_start:
                dp[i] = max(dp[i], dp[j] + 1)
                
    # 4. dp 배열 중 최댓값 출력
    print(max(dp))

if __name__ == "__main__":
    solve()