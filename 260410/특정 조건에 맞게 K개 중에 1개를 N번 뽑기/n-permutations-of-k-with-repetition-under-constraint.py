k, n = map(int, input().split())
nums = []

# 순서쌍 구성
def pick(i):
    # 출력
    if i == n:
        print(" ".join(map(str, nums)))
        return

    for j in range(1, k + 1):
        # 3번 이상 제외
        if i == 0 or i == 1 or (nums[i-1] != j or nums[i-2] != j):
            nums.append(j)
            pick(i+1)
            nums.pop()

pick(0)
