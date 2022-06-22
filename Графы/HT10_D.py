from sys import stdin, setrecursionlimit
import threading

MAX_RECURSION_DEPTH = 10 ** 9
STACK_SIZE = 2 ** 26
DEFAULT_COLOUR = 0

ans = []


def dfs_top_sort(v):
    global ans
    colour[v] = 1
    for u in edges[v]:
        if colour[u] == DEFAULT_COLOUR:
            dfs_top_sort(u)
    ans.append(v)


def dfs(v, cur_colour):
    reversed_colour[v] = cur_colour
    for u in reversed_edges[v]:
        if reversed_colour[u] == DEFAULT_COLOUR:
            dfs(u, cur_colour)


def main():
    global colour, edges, reversed_edges, reversed_colour, ans
    n, m = map(int, stdin.buffer.readline().decode().strip().split())
    colour = [DEFAULT_COLOUR for _ in range(n + 1)]
    reversed_colour = [DEFAULT_COLOUR for _ in range(n + 1)]
    edges = [set() for _ in range(n + 1)]
    reversed_edges = [set() for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, stdin.buffer.readline().decode().strip().split())
        if x != y:
            edges[x].add(y)
            reversed_edges[y].add(x)
    for i in range(1, n + 1):
        if colour[i] == DEFAULT_COLOUR:
            dfs_top_sort(i)
    ans = ans[::-1]
    cnt_components = 0
    for i in ans:
        if reversed_colour[i] == DEFAULT_COLOUR:
            cnt_components += 1
            dfs(i, cnt_components)
    condensation = [set() for _ in range(cnt_components + 1)]
    cnt_edges = 0
    for i in range(1, n + 1):
        for j in edges[i]:
            if reversed_colour[i] != reversed_colour[j] and reversed_colour[j] not in condensation[reversed_colour[i]]:
                cnt_edges += 1
                condensation[reversed_colour[i]].add(reversed_colour[j])
    print(cnt_edges)


if __name__ == "__main__":
    setrecursionlimit(MAX_RECURSION_DEPTH)
    threading.stack_size(STACK_SIZE)
    thread = threading.Thread(target=main)
    thread.start()
