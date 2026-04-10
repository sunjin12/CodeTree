n = int(input())
nums = []

# 아름다운 수 체크
def check_nums():
    i = 0
    while i < n:
        num = nums[i]
        for j in range(1, num):
            if i+j >= n or nums[i] != nums[i+j]:
                return False
        i += num
    return True

# 전체 숫자 만들기
cnt = 0
def make_nums(i):
    global cnt
    if i == n:
        if check_nums():
            cnt += 1
        return
    
    for j in range(1, 5):
        nums.append(j)
        make_nums(i+1)
        nums.pop()

make_nums(0)

print(cnt)





