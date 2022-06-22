from sys import stdin, stdout
from math import inf


class Node:
    def __init__(self, data = None, set_flag = False, upd = None):
        self.data = data
        self.set_flag = set_flag
        self.upd = upd


class SegmentTree:
    def __init__(self, lst = []):
        self.lst = lst
        self.t_arr = [Node(data=inf) for i in range(4 * len(lst))]
        self.size = None
        self.build()

    def build(self):
        x = 1
        size = len(self.lst)
        while x < size:
            x *= 2
        self.size = x
        for i in range(size):
            self.t_arr[i + x - 1].data = self.lst[i]
        for v in range(x - 2, -1, -1):
            self.t_arr[v].data = min(self.t_arr[2 * v + 1].data, self.t_arr[2 * v + 2].data)

    def rmq(self, v, left, right, query_a, query_b):

        if left > query_b or right < query_a:
            return inf

        if left >= query_a and right <= query_b:
            return self.get(v)
        if left != right:
            self.t_arr[v].data = self.get(v)
        self.push(v, left, right)
        middle = (left + right) // 2
        return min(self.rmq(2 * v + 1, left, middle, query_a, query_b),
                   self.rmq(2 * v + 2, middle + 1, right, query_a, query_b))

    def get(self, v):
        if self.t_arr[v].set_flag:
            return self.t_arr[v].upd
        elif self.t_arr[v].upd is not None:
            return self.t_arr[v].data + self.t_arr[v].upd
        else:
            return self.t_arr[v].data

    def push(self, v, left, right):
        if left == right:
            if self.t_arr[v].set_flag:
                self.t_arr[v].data = self.t_arr[v].upd
            elif self.t_arr[v].upd is not None:
                self.t_arr[v].data += self.t_arr[v].upd
        else:
            if self.t_arr[v].set_flag:
                self.t_arr[2 * v + 1].set_flag = True
                self.t_arr[2 * v + 1].upd = self.t_arr[v].upd
                self.t_arr[2 * v + 2].set_flag = True
                self.t_arr[2 * v + 2].upd = self.t_arr[v].upd
            elif self.t_arr[v].upd is not None:
                if self.t_arr[2 * v + 1].upd is not None:
                    self.t_arr[2 * v + 1].upd += self.t_arr[v].upd
                else:
                    self.t_arr[2 * v + 1].upd = self.t_arr[v].upd
                if self.t_arr[2 * v + 2].upd is not None:
                    self.t_arr[2 * v + 2].upd += self.t_arr[v].upd
                else:
                    self.t_arr[2 * v + 2].upd = self.t_arr[v].upd
            # if self.t_arr[2 * v + 1].upd is None or self.t_arr[v].set_flag:
            #     self.t_arr[2 * v + 1] = Node(self.t_arr[v].data, self.t_arr[v].set_flag, self.t_arr[v].upd)
            # else:
            #     self.t_arr[2 * v + 1].upd += self.t_arr[v].upd
            # if self.t_arr[2 * v + 2].upd is None or self.t_arr[v].set_flag:
            #     self.t_arr[2 * v + 2] = Node(self.t_arr[v].data, self.t_arr[v].set_flag, self.t_arr[v].upd)
            # else:
            #     self.t_arr[2 * v + 2].upd += self.t_arr[v].upd
            #middle = (left + right) // 2
            #self.t_arr[v].data = min(self.get(2 * v + 1), self.get(2 * v + 2))
        self.t_arr[v].set_flag = False
        self.t_arr[v].upd = None

    def update(self, v, left, right, query_a, query_b, x, add_flag):
        if left > query_b or right < query_a:
            return
        self.push(v, left, right)
        if left >= query_a and right <= query_b:
            #if (left != right):
            #    self.t_arr[v].data = min(self.get(2 * v + 1), self.get(2 * v + 2))
            self.t_arr[v].set_flag = not add_flag
            self.t_arr[v].upd = x
            return
        middle = (left + right) // 2
        self.update(2 * v + 1, left, middle, query_a, query_b, x, add_flag)
        self.update(2 * v + 2, middle + 1, right, query_a, query_b, x, add_flag)
        self.t_arr[v].data = min(self.get(2 * v + 1), self.get(2 * v + 2))
        #if left <= query_b and right >= query_a:
        #    self.t_arr[v].data = min(self.get(2 * v + 1), self.get(2 * v + 2))
        #self.t_arr[v].data = min(self.get(2 * v + 1), self.get(2 * v + 2))
        #self.t_arr[v].data = min(self.get(2 * v + 1, left, middle), self.get(2 * v + 2, middle + 1, right))

    def command(self, query):
        #for pt in self.t_arr[:15]:
        #    print(pt.data, pt.set_flag, pt.upd)
        #print()
        if query[0] == "set":
            self.update(0, 1, self.size, int(query[1]), int(query[2]), int(query[3]), False)
            return "skip"
        elif query[0] == "add":
            self.update(0, 1, self.size, int(query[1]), int(query[2]), int(query[3]), True)
            return "skip"
        else:
            return self.rmq(0, 1, self.size, int(query[1]), int(query[2]))


n = int(stdin.buffer.readline().decode())
lst = list(map(int, stdin.buffer.readline().decode().strip().split()))
my_tree = SegmentTree(lst)
ans = [str(my_tree.command(line.decode().strip().split())) for line in stdin.buffer.readlines()]
ans = '\n'.join(filter(lambda x: x != "skip", ans))
stdout.buffer.write(ans.encode())