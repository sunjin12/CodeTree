n, m = map(int, input().split())
people = list(map(int, input().split()))
coverage = 0
cnt = 0

for i in range(n):
    if people[i] == 1 and coverage == 0:
        cnt += 1
        coverage = 2 * m + 1

    if coverage > 0:
        coverage -= 1

print(cnt)



