from sys import stdin, setrecursionlimit
import threading

MAX_RECURSION_DEPTH = 10 ** 9
STACK_SIZE = 2 ** 26
DEFAULT_COLOUR = 0


ans = []
flag = True


def dfs(v):
    global ans, flag
    colour[v] = 1
    for u in edges[v]:
        if colour[u] == DEFAULT_COLOUR:
            dfs(u)
        elif colour[u] == 1:
            flag = False
    colour[v] = 2
    ans.append(v)
    if not flag:
        return -1
    else:
        return 0


def main():
    global colour, edges
    n, m = map(int, stdin.buffer.readline().decode().strip().split())
    colour = [DEFAULT_COLOUR for _ in range(n + 1)]
    edges = [set() for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, stdin.buffer.readline().decode().strip().split())
        edges[x].add(y)
    for i in range(1, n + 1):
        if colour[i] == DEFAULT_COLOUR:
            if dfs(i) == -1:
                break
    if flag:
        print(*ans[::-1])
    else:
        print(-1)


if __name__ == "__main__":
    setrecursionlimit(MAX_RECURSION_DEPTH)
    threading.stack_size(STACK_SIZE)
    thread = threading.Thread(target=main)
    thread.start()
