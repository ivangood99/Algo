from math import inf

class Edge:
    def __init__(self, u, v, cap, flow):
        self.u = u
        self.v = v
        self.cap = cap
        self.flow = flow


def push_flow(v, t, cur_flow, used):
    global edges
    used[v] = True
    if v == t:
        return cur_flow
    for cur_edge in edges[v]:
        if cur_edge is not None:
        #cur_edge is from v to cur_edge.v
            if not used[cur_edge.v] and cur_edge.flow < cur_edge.cap:
                next_flow = min(cur_flow, cur_edge.cap - cur_edge.flow)
                print(next_flow)
                delta = push_flow(cur_edge.v, t, next_flow, used)
                if delta > 0:
                    edges[cur_edge.v][cur_edge.u].flow += delta
                    edges[cur_edge.u][cur_edge.v].flow -= delta
                    return delta
    return 0


def ford_fulkerson(start, finish):
    ans = 0
    while True:
        used = [False for _ in range(n + 1)]
        delta = push_flow(start, finish, inf, used)
        if delta > 0:
            ans += delta
        else:
            break
    return ans


n = int(input())
m = int(input())
edges = [[None for i in range(n + 1)] for _ in range(n + 1)]
for i in range(m):
    u, v, cap = map(int, input().split())
    u, v = min(u, v), max(u, v)
    if edges[u][v] is None:
        edges[u][v] = Edge(u, v, cap, 0)
        edges[v][u] = Edge(v, u, 0, 0)
    else:
        edges[u][v].cap += cap
print(ford_fulkerson(1, n))