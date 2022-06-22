from sys import stdin, stdout


class Node:
    def __init__(self, i = 0):
        self.prev = i
        self.rang = 0
        self.xp = 0


class DSU:
    def __init__(self, n):
        self.arr = [Node(i) for i in range(n + 1)]

    def get(self, x):
        if self.arr[x].prev != x:
            cur_xp = self.get_xp(x)
            self.arr[x].prev = self.get(self.arr[x].prev)
            self.arr[x].xp = cur_xp - self.arr[self.arr[x].prev].xp
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
        self.arr[x].xp -= self.arr[y].xp

    def add(self, x, pts):
        self.arr[self.get(x)].xp += pts

    def get_xp(self, x):
        ans = self.arr[x].xp
        while self.arr[x].prev != x:
            x = self.arr[x].prev
            ans += self.arr[x].xp
        return ans

    def command(self, query):
        if query[0] == "join":
            self.join(int(query[1]), int(query[2]))
            return "skip"
        elif query[0] == "get":
            result = self.get_xp(int(query[1]))
            return str(result)
        else:
            self.add(int(query[1]), int(query[2]))
            return "skip"


n, m = map(int, stdin.buffer.readline().decode().strip().split())
my_dsu = DSU(n)
ans = [my_dsu.command(line.decode().strip().split()) for line in stdin.buffer.readlines()]
ans = '\n'.join(filter(lambda x: x != "skip", ans))
stdout.buffer.write(ans.encode())
