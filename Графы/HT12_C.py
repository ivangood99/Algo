from sys import stdin
from math import inf, sqrt


def calc_weight(point1, point2):
    return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


n = int(stdin.buffer.readline().decode())
points = []
for i in range(n):
    x, y = map(int, stdin.buffer.readline().decode().strip().split())
    points.append((x, y))
weights = [inf for _ in range(n)]
used = [False for _ in range(n)]
weights[0] = 0
for i in range(n):
    nxt = -1
    for v in range(n):
        if not used[v] and (nxt == -1 or weights[v] < weights[nxt]):
            nxt = v
    used[nxt] = True
    for to in range(n):
        if not used[to]:
            w = calc_weight(points[to], points[nxt])
            if w < weights[to]:
                weights[to] = w
print(sum(weights[:]))
