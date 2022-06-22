#for_check_tl
from sys import stdin, stdout


class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class Linked_List:
    def __init__(self):
        self.size = 0
        self.head = None

    def insert(self, x):
        if self.size == 0:
            node = Node(x)
            self.head = node
        else:
            node = Node(min(self.head.data, x), self.head)
            self.head = node
        self.size += 1

    def erase(self):
        min_el = self.head.data
        if self.size == 1:
            self.head = None
        else:
            self.head = self.head.next
        self.size -= 1
        return min_el

class Stack:
    def __init__(self):
        self.size = 0
        self.elements = Linked_List()

    def push(self, x):
        self.elements.insert(x)

    def pop(self):
        return self.elements.erase()

    def find_min(self):
        ans = self.pop()
        self.push(ans)
        return ans

    def command(self, query):
        if query[0] == '1':
            self.push(int(query[1]))
            return None
        elif query[0] == '2':
            self.pop()
            return None
        else:
            return str(self.find_min())


n = int(stdin.buffer.readline().decode())
stack = Stack()
ans = [stack.command(line.decode().strip().split()) for line in stdin.buffer.readlines()]
ans = '\n'.join(filter(lambda x: x is not None, ans))
stdout.buffer.write(ans.encode())

