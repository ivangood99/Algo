from sys import stdin
from math import inf


def check_way(start, finish):
    global edges
    used = [False for _ in range(n + 1)]
    queue = [start]
    used[start] = True
    while len(queue) > 0:
        nxt = queue.pop(0)
        for v, w in edges[nxt]:
            if not used[v]:
                used[v] = True
                queue.append(v)
    return used[finish]


n, m, start = map(int, stdin.buffer.readline().decode().strip().split())
edges = [set() for _ in range(n + 1)]
for _ in range(m):
    x, y, w = map(int, stdin.buffer.readline().decode().strip().split())
    edges[x].add((y, w))
dist = [inf for _ in range(n + 1)]
prev = [None for _ in range(n + 1)]
dist[start] = 0
for k in range(n):
    for u in range(1, n + 1):
        for v, w in edges[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                prev[v] = u
bad_v = set()
for u in range(1, n + 1):
    for v, w in edges[u]:
        if dist[v] > dist[u] + w:
            key = v
            for i in range(n):
                v = prev[v]
            cur = v
            while prev[cur] != v:
                bad_v.add(cur)
                cur = prev[cur]
            bad_v.add(cur)
for v in range(1, n + 1):
    if dist[v] != inf:
        check_flag = True
        for p in bad_v:
            if check_way(start, p) and check_way(p, v):
                check_flag = False
                break
        if check_flag:
            print(dist[v])
        else:
            print('-')
    else:
        print('*')