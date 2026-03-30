n, m = map(int, input().split())
s = input()

commands = []
for _ in range(m):
    cmd = input().split()
    if len(cmd) == 1:
        commands.append((cmd[0],))
    else:
        commands.append((cmd[0], cmd[1]))

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.END = Node(-1)
        self.head = self.END
        self.tail = self.END

    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        self.head.prev = new_node
        self.head = new_node
        new_node.prev = None
    
    def push_back(self, new_data):
        if self.begin() == self.end():
            self.push_front(new_data)
        
        else:
            new_node = Node(new_data)
            new_node.prev = self.tail.prev
            self.tail.prev.next = new_node
            new_node.next = self.tail
            self.tail.prev = new_node
    
    def erase(self, node):
        next_node = node.next

        if node == self.begin():
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            temp.next = None
        
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.next = None
        
        return next_node
    
    def insert(self, node, new_data):
        if node == self.end():
            self.push_back(new_data)
        
        elif node == self.begin():
            self.push_front(new_data)
        
        else:
            new_node = Node(new_data)
            new_node.prev = node.prev
            new_node.next = node
            node.prev.next = new_node
            node.prev = new_node
        
    def begin(self):
        return self.head
    
    def end(self):
        return self.tail

dll = DoublyLinkedList()

for c in s:
    dll.push_back(c)

it = dll.end()

for command in commands:
    if command[0] == 'L':
        if it == dll.begin():
            pass
        else:
            it = it.prev
    
    elif command[0] == 'R':
        if it == dll.end():
            pass
        else:
            it = it.next
    
    elif command[0] == 'D':
        if it == dll.end():
            pass
        else:
            dll.erase(it)

    elif command[0] == 'P':
        dll.insert(it, command[1])

    else:
        print("wrong input")

it = dll.begin()
while it != dll.end():
    print(it.data, end = '')
    it = it.next