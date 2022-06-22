from sys import stdin, setrecursionlimit
import threading

MAX_RECURSION_DEPTH = 10 ** 9
STACK_SIZE = 2 ** 26
DEFAULT_COLOUR = 0

order = []
time = 1


def dfs(v):
    global time
    colour[v] = 1
    tin[v] = time
    order.append(v)
    for u in edges[v]:
        if colour[u] == DEFAULT_COLOUR:
            time += 1
            tree_edges[v].add(u)
            tree_edges[u].add(v)
            dfs(u)


def main():
    global colour, edges, tin, order, tree_edges
    n, m = map(int, stdin.buffer.readline().decode().strip().split())
    colour = [DEFAULT_COLOUR for _ in range(n + 1)]
    edges = [set() for _ in range(n + 1)]
    tree_edges = [set() for _ in range(n + 1)]
    tin = [-1 for _ in range(n + 1)]
    up = [n + 1 for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, stdin.buffer.readline().decode().strip().split())
        if x != y:
            edges[x].add(y)
            edges[y].add(x)
    roots = []
    for i in range(1, n + 1):
        if colour[i] == DEFAULT_COLOUR:
            dfs(i)
            roots.append(i)

    for i in order[::-1]:
        up[i] = tin[i]
        for j in tree_edges[i]:
            if up[j] < up[i] and tin[j] > tin[i]:
                up[i] = up[j]
        for j in edges[i]:
            if j not in tree_edges[i] and tin[j] < up[i] and tin[j] < tin[i]:
                up[i] = tin[j]
    ans = []
    for i in roots:
        if len(tree_edges[i]) > 1:
            ans.append(i)
    for i in range(1, n + 1):
        if i not in roots:
            flag = False
            for j in tree_edges[i]:
                if up[j] >= tin[i] and tin[j] > tin[i]:
                    flag = True
            if flag:
                ans.append(i)
    print(len(ans))
    print(*sorted(ans))




if __name__ == "__main__":
    setrecursionlimit(MAX_RECURSION_DEPTH)
    threading.stack_size(STACK_SIZE)
    thread = threading.Thread(target=main)
    thread.start()
