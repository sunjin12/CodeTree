N = int(input())

command = []
stack = []
num = 0

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push_back" or line[0] == "get":
        num = int(line[1])
    
    if line[0] == "push_back":
        stack.append(num)
    elif line[0] == "pop_back":
        stack.pop()
    elif line[0] == "size":
        print(len(stack))
    else:
        print(stack[num - 1])


# Please write your code here.
