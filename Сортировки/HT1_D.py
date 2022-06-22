n_inv = 0

def merge(a, b):
    res = []
    i, j = 0, 0
    global n_inv
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
            n_inv += len(a) - i
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
merge_sort(arr)
print(n_inv)