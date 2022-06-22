from sys import stdin, stdout


class BinaryIndexedTree:
    def __init__(self, lst = []):
        self.lst = lst
        self.t_arr = [0 for k in range(len(self.lst))]
        self.build()

    def F(self, i):
        return i & (i + 1)

    def build(self):
        for i in range(len(self.lst)):
            self.add(i, self.lst[i])

    def set(self, i, elem):
        diff = elem - lst[i]
        self.lst[i] = elem
        self.add(i, diff)

    def add(self, i, elem):
        while i < len(self.lst):
            self.t_arr[i] += elem
            i = i | (i + 1)

    def get_sum(self, i):
        res = 0
        while i >= 0:
            res += self.t_arr[i]
            i = self.F(i) - 1
        return res

    def rsq(self, l, r):
        if l == 0:
            return self.get_sum(r)
        else:
            return self.get_sum(r) - self.get_sum(l - 1)

    def command(self, query):
        if query[0] == "set":
            self.set(int(query[1]) - 1, int(query[2]))
            return "skip"
        else:
            return self.rsq(int(query[1]) - 1, int(query[2]) - 1)


n = int(stdin.buffer.readline().decode())
lst = list(map(int, stdin.buffer.readline().decode().strip().split()))
my_tree = BinaryIndexedTree(lst)
ans = [str(my_tree.command(line.decode().strip().split())) for line in stdin.buffer.readlines()]
ans = '\n'.join(filter(lambda x: x != "skip", ans))
stdout.buffer.write(ans.encode())