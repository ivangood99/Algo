MAX_LEN = 10 ** 9

def count_ropes(ropes, middle):
    ans = 0
    if middle == 0:
        return 0
    for rope in ropes:
        ans += rope // middle
    return ans


def solve(ropes, k):
    left = 0
    right = MAX_LEN
    while right > left + 1:
        middle = (left + right) // 2
        if count_ropes(ropes, middle) < k:
            right = middle
        else:
            left = middle
    return left


n, k = map(int, input().split())
ropes = []
for _ in range(n):
    ropes.append(int(input()))
print(solve(ropes, k))
