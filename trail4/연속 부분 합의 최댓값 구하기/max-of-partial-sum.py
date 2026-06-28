import sys

def solve():
    # 입력 받기
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    n = int(data[0])
    arr = list(map(int, data[1:]))
    
    # dp_current: 현재 위치를 끝으로 하는 연속 부분 합의 최댓값
    # max_ans: 전체 구간 중 발견한 연속 부분 합의 최댓값
    dp_current = arr[0]
    max_ans = arr[0]
    
    # 두 번째 원소부터 끝까지 순회
    for i in range(1, n):
        # 직전까지의 합에 현재 원소를 더한 것과, 현재 원소 자체를 비교
        dp_current = max(arr[i], dp_current + arr[i])
        # 전체 최댓값 갱신
        max_ans = max(max_ans, dp_current)
        
    print(max_ans)

if __name__ == "__main__":
    solve()