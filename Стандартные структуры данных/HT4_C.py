import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


class Queue:
    def __init__(self):
        self.first = -1
        self.last = 0
        self.size = 0
        self.capacity = 1
        self.lst = [0]

    def rearrange(self, capacity):
        new_lst = [0 for _ in range(capacity)]
        for i in range(0, self.size):
            new_lst[i] = self.lst[(i + self.first) % self.capacity]
        self.lst = new_lst
        self.first = 0
        self.last = self.size

    def ensureCapacity(self):
        self.rearrange(self.capacity * 2)
        self.capacity *= 2

    def decreaseCapacity(self):
        self.rearrange(self.capacity // 2)
        self.capacity //= 2

    def add(self, x):
        if self.size == self.capacity:
            self.ensureCapacity()
        self.lst[self.last] = x
        self.last = (self.last + 1) % self.capacity
        self.size += 1
        if self.first == -1:
            self.first = 0

    def delete(self):
        deleted = self.lst[self.first]
        self.first = (self.first + 1) % self.capacity
        self.size -= 1
        if (self.size <= self.capacity // 4 and self.size != 0):
            self.decreaseCapacity()
        if self.first == self.last:
            self.first = -1
            self.last = 0
        return deleted

n = int(input())
queue = Queue()
for _ in range(n):
    query = list(map(str, input().split()))
    if query[0] == "+":
        queue.add(int(query[1]))
    else:
        print(queue.delete())



