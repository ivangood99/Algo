import random

def split(arr, left, right, x):
    m_l = left
    m_le = left
    for i in range(left, right):
        if arr[i] < x:
            arr[i], arr[m_l] = arr[m_l], arr[i]
            if m_le > m_l:
                arr[i], arr[m_le] = arr[m_le], arr[i]
            m_l += 1
            m_le += 1
        elif arr[i] == x:
            arr[i], arr[m_le] = arr[m_le], arr[i]
            m_le += 1
    return m_l, m_le

def solve(arr, left, right, k):
    if right - left == 1:
        return arr[left]
    x = random.choice(arr[left:right])
    m_l, m_le = split(arr, left, right, x)
    if k >= left and k < m_l:
        return solve(arr, left, m_l, k)
    elif k >= m_l and k < m_le:
        return arr[m_l]
    else:
        return solve(arr, m_le, right, k)


n = int(input())
arr = list(map(int, input().split()))
m = int(input())
for query in range(m):
    i, j, k = map(int, input().split())
    print(solve(arr[i - 1 : j], 0, j - i + 1, k - 1))