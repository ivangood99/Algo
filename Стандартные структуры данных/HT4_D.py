import fileinput

class MyHeap:
    def __init__(self):
        self.size = 0
        self.lst = []
        self.locations = []

    def push(self, x):
        pos = len(self.locations)
        self.locations.append(self.size)
        self.lst.append((x, pos))
        self.sift_up(self.size)
        self.size += 1

    def extract_min(self):
        self.locations.append(-1)
        if self.size == 0:
            return "*"
        extracted_min = self.lst[0]
        self.size -= 1
        self.swap(0, self.size)
        self.lst.pop()
        self.sift_down(0)
        self.locations[extracted_min[1]] = -1
        return extracted_min

    def decrease(self, p, x):
        self.locations.append(-1)
        if len(self.locations) >= p and self.locations[p - 1] != -1:
            i = self.locations[p - 1]
            self.lst[i] = (x, p - 1)
            self.sift_up(i)

    def sift_up(self, ind):
        while ind > 0 and self.lst[(ind - 1) // 2][0] > self.lst[ind][0]:
            self.swap(ind, (ind - 1) // 2)
            ind = (ind - 1) // 2

    def sift_down(self, ind):
        while 2 * ind + 1 < self.size:
            left = 2 * ind + 1
            right = 2 * ind + 2
            if right >= self.size or self.lst[left] < self.lst[right]:
                min_son = left
            else:
                min_son = right
            if self.lst[min_son] < self.lst[ind]:
                self.swap(ind, min_son)
                ind = min_son
            else:
                break

    def swap(self, i, j):
        self.locations[self.lst[i][1]] = j
        self.locations[self.lst[j][1]] = i
        self.lst[i], self.lst[j] = self.lst[j], self.lst[i]


heap = MyHeap()
for query in fileinput.input():
    lst = list(map(str, query.split()))
    if lst[0] == "push":
        heap.push(int(lst[1]))
    elif lst[0] == "extract-min":
        ans = heap.extract_min()
        if ans == "*":
            print(ans)
        else:
            print(ans[0], ans[1] + 1)
    else:
        heap.decrease(int(lst[1]), int(lst[2]))