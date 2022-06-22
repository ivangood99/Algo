from sys import stdin, stdout

PRIME_NUMBER = 31
MOD_NUMBER = 10 ** 9


def get_hash(left, right):
    global hash_lst, powp
    if left == 0:
        return hash_lst[right]
    return (hash_lst[right] - (hash_lst[left - 1] * powp[right - left + 1]) % MOD_NUMBER + MOD_NUMBER) % MOD_NUMBER


def init(s):
    global hash_lst, powp
    hash_lst[0] = ord(s[0])
    powp[0] = 1
    for i in range(1, len(s)):
        hash_lst[i] = (hash_lst[i - 1] * PRIME_NUMBER + ord(s[i])) % MOD_NUMBER
        powp[i] = (powp[i - 1] * PRIME_NUMBER) % MOD_NUMBER


s = stdin.buffer.readline().decode().strip()
hash_lst = [0 for _ in range(len(s))]
powp = [0 for _ in range(len(s))]
init(s)
n = int(stdin.buffer.readline().decode().strip())
ans = []
for line in stdin.buffer.readlines():
    l1, r1, l2, r2 = map(int, line.decode().strip().split())
    if get_hash(l1 - 1, r1 - 1) == get_hash(l2 - 1, r2 - 1):
        ans.append('Yes')
    else:
        ans.append('No')
ans = '\n'.join(ans)
stdout.buffer.write(ans.encode())