from sys import stdin, setrecursionlimit
import threading

MAX_RECURSION_DEPTH = 10 ** 9
STACK_SIZE = 2 ** 26
DEFAULT_COLOUR = 0


def dfs(v, cur_colour):
    colour[v] = cur_colour
    for u in edges[v]:
        if colour[u] == DEFAULT_COLOUR:
            dfs(u, cur_colour)


def main():
    global colour, edges
    n, m = map(int, stdin.buffer.readline().decode().strip().split())
    colour = [DEFAULT_COLOUR for _ in range(n + 1)]
    edges = [set() for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, stdin.buffer.readline().decode().strip().split())
        edges[x].add(y)
        edges[y].add(x)
    cnt = 0
    for i in range(1, n + 1):
        if colour[i] == DEFAULT_COLOUR:
            cnt += 1
            dfs(i, cnt)
    print(cnt)
    print(*colour[1:])


if __name__ == "__main__":
    setrecursionlimit(MAX_RECURSION_DEPTH)
    threading.stack_size(STACK_SIZE)
    thread = threading.Thread(target=main)
    thread.start()
