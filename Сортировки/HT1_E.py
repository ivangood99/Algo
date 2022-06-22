import random

def split(left, right, x, arr):
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

def qsort(left, right, arr):
    if right - left <= 1:
        return
    x = random.choice(arr[left:right])
    m_l, m_le = split(left, right, x, arr)
    qsort(left, m_l, arr)
    qsort(m_le, right, arr)

N = int(input())
arr = list(map(int, input().split()))
qsort(0, len(arr), arr)
print(*arr)