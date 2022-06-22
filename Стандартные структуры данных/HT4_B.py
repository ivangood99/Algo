class Stack:
    def __init__(self):
        self.length = 0
        self.lst = [0]
        self.capacity = 1

    def ensureCapacity(self):
        self.capacity *= 2
        new_lst = [0 for _ in range(self.capacity)]
        for i in range(self.length):
            new_lst[i] = self.lst[i]
        self.lst = new_lst

    def decreaseCapacity(self):
        self.capacity = self.capacity // 2

    def push(self, x):
        if self.length == self.capacity:
            self.ensureCapacity()
        self.lst[self.length] = x
        self.length += 1

    def pop(self):
        self.length -= 1
        if (self.length <= self.capacity / 4):
            self.decreaseCapacity()
        return self.lst[self.length]


lst = list(map(str, input().split()))
stack = Stack()
for i in range(len(lst)):
    if lst[i] in ['+', "-", "*"]:
        second = stack.pop()
        first = stack.pop()
        if lst[i] == "+":
            stack.push(first + second)
        elif lst[i] == "-":
            stack.push(first - second)
        else:
            stack.push(first * second)
    else:
        stack.push(int(lst[i]))
print(stack.pop())