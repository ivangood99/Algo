def get_cells(pt, n):
    good_cells = []
    good = range(1, n + 1)
    if pt[0] + 1 in good and pt[1] + 2 in good:
        good_cells.append((pt[0] + 1, pt[1] + 2))
    if pt[0] + 2 in good and pt[1] + 1 in good:
        good_cells.append((pt[0] + 2, pt[1] + 1))
    if pt[0] + 2 in good and pt[1] - 1 in good:
        good_cells.append((pt[0] + 2, pt[1] - 1))
    if pt[0] + 1 in good and pt[1] - 2 in good:
        good_cells.append((pt[0] + 1, pt[1] - 2))
    if pt[0] - 1 in good and pt[1] - 2 in good:
        good_cells.append((pt[0] - 1, pt[1] - 2))
    if pt[0] - 2 in good and pt[1] - 1 in good:
        good_cells.append((pt[0] - 2, pt[1] - 1))
    if pt[0] - 2 in good and pt[1] + 1 in good:
        good_cells.append((pt[0] - 2, pt[1] + 1))
    if pt[0] - 1 in good and pt[1] + 2 in good:
        good_cells.append((pt[0] - 1, pt[1] + 2))
    return good_cells


def bfs(n, start, finish):
    queue = [start]
    used = [[0] * (n + 1) for _ in range(n + 1)]
    dist = [[0] * (n + 1) for _ in range(n + 1)]
    prev = [[None] * (n + 1) for _ in range(n + 1)]
    dist[start[0]][start[1]] = 1
    while len(queue) > 0:
        v = queue.pop(0)
        for u in get_cells(v, n):
            if not used[u[0]][u[1]]:
                used[u[0]][u[1]] = 1
                dist[u[0]][u[1]] = dist[v[0]][v[1]] + 1
                prev[u[0]][u[1]] = v
                queue.append(u)
    way = []
    cur = finish
    while cur != start:
        way.append(cur)
        cur = prev[cur[0]][cur[1]]
    way.append(cur)
    return way[::-1]


n = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
ans = bfs(n, (x1, y1), (x2, y2))
print(len(ans))
for cell in ans:
    print(cell[0], cell[1])
