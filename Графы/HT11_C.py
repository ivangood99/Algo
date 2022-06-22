from math import inf

NO_EDGE_VALUE = 10 ** 5

n = int(input())
dist = []
nxt = [list(range(n)) for _ in range(n)]

for i in range(n):
    row = list(map(int, input().split()))
    for k in range(n):
        if row[k] == NO_EDGE_VALUE:
            row[k] = inf
    dist.append(row)

for k in range(n):
    for u in range(n):
        for v in range(n):
            if dist[u][v] > dist[u][k] + dist[k][v]:
                dist[u][v] = dist[u][k] + dist[k][v]
                nxt[u][v] = nxt[u][k]
print(nxt)
start = -1
for v in range(n):
    if dist[v][v] < 0:
        cur = nxt[v][v]
        start = v
        break
if start == -1:
    print('NO')
else:
    print('YES')
    ans = [cur + 1]
    while cur != start:
        if (nxt[cur][cur] + 1) in ans:
            ans = ans[ans.index(nxt[cur][cur] + 1):]
            break
        cur = nxt[cur][cur]
        ans.append(cur + 1)
    print(len(ans))
    print(*ans)
