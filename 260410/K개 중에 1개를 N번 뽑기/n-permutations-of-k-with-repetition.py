k, n = map(int, input().split())
answer = []

def print_answer() -> None:
    for elem in answer:
        print(elem, end=' ')
    print()

    return

def pick_i(i):
    if i == n+1:
        print_answer()
        return

    for j in range(1, k+1):
        answer.append(j)
        pick_i(i+1)
        answer.pop()

pick_i(1)



