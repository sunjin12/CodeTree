import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
    
    n = int(data[0])
    arr = [int(x) for x in data[1:n+1]]
    
    total_sum = sum(arr)
    
    # 1. 전체 합이 홀수라면 정확히 반으로 나누는 것이 절대 불가능합니다.
    if total_sum % 2 != 0:
        print("No")
        return
        
    target = total_sum // 2
    
    # dp[j]: 원소들을 조합하여 합 j를 만들 수 있는지 여부
    dp = [False] * (target + 1)
    dp[0] = True  # 아무것도 선택하지 않았을 때 합 0 달성 가능
    
    # 2. 0/1 배낭 문제 방식으로 부분집합의 합 탐색
    for num in arr:
        # 중복 선택을 방지하기 위해 target부터 역순으로 내려옵니다.
        for j in range(target, num - 1, -1):
            if dp[j - num]:
                dp[j] = True
                
        # 중간에 이미 target을 만들 수 있게 되었다면 조기 종료(Optimization)
        if dp[target]:
            print("Yes")
            return

    # 3. 최종 결과 출력
    if dp[target]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()