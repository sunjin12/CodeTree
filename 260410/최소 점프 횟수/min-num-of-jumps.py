n = int(input())
num = [0] + list(map(int, input().split()))
min_jumps = [-1] * (n+1)

# i번째에서 갈 수 있는 자리들 계산
def jump(i, jumps):
    min_jumps[i] = jumps
    # i == n이면 최솟값 확인
    if i == n:
        if min_jumps[n] == -1:
            min_jumps[n] = jumps
        else:
            min_jumps[n] = min(min_jumps[n], jumps)
        return

    for j in range(1, num[i]+1):
        if min_jumps[i+j] == -1 or min_jumps[i+j] > jumps + 1:
            jump(i+j, jumps+1)
   
jump(1, 0)

# 최소 점프 출력
print(min_jumps[n])