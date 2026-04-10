n = int(input())
num = [0] + list(map(int, input().split()))
min_jumps = [-1] * (n + 1)

def jump(i, jumps):
    # 끝 지점에 도달하면 탐색 종료 (이미 아래 for문에서 최소값 갱신을 마침)
    if i == n:
        return

    for j in range(1, num[i] + 1):
        # 수정 1: 점프한 위치(i + j)가 n을 넘지 않도록 경계값 체크
        if i + j <= n:
            # 수정 2: 방문하지 않았거나, 기존보다 더 적은 점프로 도달 가능한 경우만 탐색
            if min_jumps[i + j] == -1 or min_jumps[i + j] > jumps + 1:
                min_jumps[i + j] = jumps + 1  # 큐/스택에 넣기 전에 방문 처리 및 최소값 갱신
                jump(i + j, jumps + 1)

# 시작 위치 초기화
min_jumps[1] = 0
jump(1, 0)

# 최소 점프 출력
print(min_jumps[n])