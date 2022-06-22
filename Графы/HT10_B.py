from sys import stdin, setrecursionlimit
import threading

MAX_RECURSION_DEPTH = 10 ** 9
STACK_SIZE = 2 ** 26
DEFAULT_COLOUR = 0

max_len = 1


def dfs(v, cur_len):
    global max_len
    if cur_len > max_len:
        max_len = cur_len
    for u in edges[v]:
        if colour[u] == DEFAULT_COLOUR:
            dfs(u, cur_len + 1)


def main():
    global colour, edges, max_len
    n = int(input())
    dct = dict()
    colour = [DEFAULT_COLOUR for _ in range(n + 1)]
    edges = [set() for _ in range(n + 1)]
    for i in range(n):
        name1, r, name2 = map(str, input().split())
        name1 = name1.lower()
        name2 = name2.lower()
        if i == 0:
            dct[name2] = 0
        dct[name1] = i + 1
        edges[dct[name2]].add(dct[name1])
    dfs(0, 1)
    print(max_len)


if __name__ == "__main__":
    setrecursionlimit(MAX_RECURSION_DEPTH)
    threading.stack_size(STACK_SIZE)
    thread = threading.Thread(target=main)
    thread.start()
