import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    N = int(data[0])
    nums = [int(x) for x in data[1:N+1]]
    
    # 전체 숫자의 총합 구하기
    total_sum = sum(nums)
    
    # 우리가 타겟으로 삼을 배낭의 최대 용량 (총합의 절반)
    target = total_sum // 2
    
    # dp[j]: 숫자들의 조합으로 정확히 합 j를 만들 수 있는지 여부 (True/False)
    dp = [False] * (target + 1)
    dp[0] = True # 0은 아무것도 선택하지 않으면 만들 수 있으므로 항상 True
    
    # 0-1 배낭 문제 스타일로 DP 테이블 채우기
    for num in nums:
        # 숫자를 한 번씩만 고를 수 있으므로 역순(뒤에서부터)으로 탐색
        for j in range(target, num - 1, -1):
            if dp[j - num]:
                dp[j] = True
                
    # target(S//2) 이하 중에서 만들 수 있는 가장 큰 합(A) 찾기
    max_A = 0
    for j in range(target, -1, -1):
        if dp[j]:
            max_A = j
            break
            
    # 그룹 A의 합이 max_A라면, 그룹 B의 합은 (total_sum - max_A)가 됩니다.
    # 두 그룹의 최솟값 차이 출력
    group_B = total_sum - max_A
    print(abs(max_A - group_B))

if __name__ == '__main__':
    solve()