from collections import deque

# 변수 선언 및 입력:
n = int(input())
dq = deque()

for _ in range(n):
    command = input()
    if command.startswith("push_front"):
        x = int(command.split()[1])
        dq.appendleft(x)
    elif command.startswith("push_back"):
        x = int(command.split()[1])
        dq.append(x)
    elif command == "pop_front":
        print(dq.popleft())
    elif command == "pop_back":
        print(dq.pop())
    elif command == "size":
        print(len(dq))
    elif command == "empty":
        print(1 if not dq else 0)
    elif command == "front":
        print(dq[0])
    else:
        print(dq[-1])
