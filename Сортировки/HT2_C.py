N_ASCII_SYMBOLS = 128

def radix_sort(arr, n, order, phase):
    cnt = [0 for i in range(N_ASCII_SYMBOLS)]
    for i in range(n):
        cnt[ord(arr[i][-phase])] += 1
    ptr = [0]
    for i in range(N_ASCII_SYMBOLS):
        ptr.append(ptr[i] + cnt[i])
    new_order = [-1 for i in range(n)]
    for j in range(n):
        new_order[ptr[ord(arr[order[j]][-phase])]] = order[j]
        ptr[ord(arr[order[j]][-phase])] += 1
    return new_order

n, m, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(input())
order = [i for i in range(n)]
for phase in range(1, k + 1):
    order = radix_sort(arr, n, order, phase)
for i in range(n):
    print(arr[order[i]])