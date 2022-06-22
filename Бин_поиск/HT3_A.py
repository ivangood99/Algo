def bin_search(arr, n, x):
    left, right = -1, n
    while right - left > 1:
        middle = (left + right) // 2
        if arr[middle] >= x:
            right = middle
        else:
            left = middle
    if right == n:
        return arr[right - 1]
    elif right == 0:
        return arr[right]
    elif abs(arr[right] - x) < abs(arr[right - 1] - x):
        return arr[right]
    else:
        return arr[right - 1]


n, k = map(int, input().split())
arr = list(map(int, input().split()))
queries = list(map(int, input().split()))
for i in range(k):
    print(bin_search(arr, n, queries[i]))