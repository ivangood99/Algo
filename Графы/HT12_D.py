from sys import stdin, stdout


class Node:
    def __init__(self, i = 0):
        self.prev = i
        self.rang = 0


class DSU:
    def __init__(self, n):
        self.arr = [Node(i) for i in range(n + 1)]

    def get(self, x):
        if self.arr[x].prev != x:
            self.arr[x].prev = self.get(self.arr[x].prev)
        return self.arr[x].prev

    def join(self, x, y):
        x = self.get(x)
        y = self.get(y)
        if x == y:
            return
        if self.arr[x].rang > self.arr[y].rang:
            x, y = y, x
        if self.arr[x].rang == self.arr[y].rang:
            self.arr[y].rang += 1
        self.arr[x].prev = y


n, m = map(int, stdin.buffer.readline().decode().strip().split())
my_dsu = DSU(n)
edges = []
for line in stdin.buffer.readlines():
    u, v, w = map(int, line.decode().strip().split())
    edges.append((u, v, w))
edges.sort(key=lambda tup: tup[2])
ans = 0
for u, v, w in edges:
    if my_dsu.get(u) != my_dsu.get(v):
        ans += w
        my_dsu.join(u, v)
print(ans)
