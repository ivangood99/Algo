from sys import stdin
from math import inf
import heapq

n, m = map(int, stdin.buffer.readline().decode().strip().split())
edges = [set() for _ in range(n + 1)]
for _ in range(m):
    x, y, w = map(int, stdin.buffer.readline().decode().strip().split())
    edges[x].add((y, w))
    edges[y].add((x, w))
dist = [inf for _ in range(n + 1)]
dist[1] = 0
queue = []
heapq.heappush(queue, (0, 1))
cnt = 0
while cnt < n:
    min_pair = heapq.heappop(queue)
    if min_pair[0] > dist[min_pair[1]]:
        continue
    cnt += 1
    nxt = min_pair[1]
    for v, w in edges[nxt]:
        if dist[nxt] + w < dist[v]:
            dist[v] = dist[nxt] + w
            heapq.heappush(queue, (dist[v], v))
print(*dist[1:])
