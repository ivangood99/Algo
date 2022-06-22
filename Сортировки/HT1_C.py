def merge(a, b):
    res = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    res += a[i:] + b[j:]
    return res


def merge_sort(a):
    if len(a) <= 1:
        return a[:]
    else:
        left = a[: len(a) // 2]
        right = a[len(a) // 2:]
    return merge(merge_sort(left), merge_sort(right))


N = int(input())
arr = list(map(int, input().split()))
print(*merge_sort(arr))