def solve(x, y, n):
    left = -1
    right = max(x, y) * n
    min_time = min(x, y)
    while right > left + 1:
        middle = (left + right) // 2
        if (middle - min_time) // x + (middle - min_time) // y >= n - 1:
            right = middle
        else:
            left = middle
    return right


n, x, y = map(int, input().split())
print(solve(x, y, n))