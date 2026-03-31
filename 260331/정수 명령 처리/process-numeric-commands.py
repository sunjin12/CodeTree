N = int(input())

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def empty(self):
        return not self.items
    
    def size(self):
        return len(self.items)

    def top(self):
        if self.empty():
            raise Exception("Stack is empty")
        
        return self.items[-1]

    def pop(self):
        if self.empty():
            raise Exception("Stack is empty")

        return self.items.pop()
    
st = Stack()

for _ in range(N):
    line = input().split()
    if line[0] == "push":
        st.push(line[1])
    elif line[0] == "empty":
        if st.empty():
            print(1)
        else:
            print(0)
    elif line[0] == "size":
        print(st.size())
    elif line[0] == "top":
        print(st.top())
    elif line[0] == "pop":
        print(st.pop())
    else:
        raise Exception("wrong input")   
    
    
        

