from sys import stdin, stdout

TABLE_SIZE = 3 * 10 ** 6
PRIME_NUMBER = TABLE_SIZE + 17
MULTIPLIER_NUMBER = 31


class HashSet:
    def __init__(self):
        self.table = [None for _ in range(TABLE_SIZE)]

    def my_hash(self, x):
        return (MULTIPLIER_NUMBER * x % PRIME_NUMBER) % TABLE_SIZE

    def handle_query(self, query):
        if query[0][0] == 'i':
            self.insert(int(query[1]))
            return 0
        elif query[0][0] == 'e':
            if self.exists(int(query[1])):
                return True
            else:
                return False
        else:
            self.delete(int(query[1]))
            return 0

    def insert(self, x):
        hash_res = self.my_hash(x)
        exists_flag = False
        while self.table[hash_res] is not None:
            if self.table[hash_res] == x:
                exists_flag = True
                break
            hash_res = (hash_res + 1) % TABLE_SIZE
        if not exists_flag:
            self.table[hash_res] = x

    def exists(self, x):
        hash_res = self.my_hash(x)
        while self.table[hash_res] is not None:
            if self.table[hash_res] == x:
                return True
            hash_res = (hash_res + 1) % TABLE_SIZE
        return False

    def delete(self, x):
        hash_res = self.my_hash(x)
        while self.table[hash_res] is not None:
            if self.table[hash_res] == x:
                self.table[hash_res] = None
                j = (hash_res + 1) % TABLE_SIZE
                while self.table[j] is not None:
                    if self.my_hash(self.table[j]) <= hash_res or self.my_hash(self.table[j]) > j:
                        self.table[hash_res], self.table[j] = self.table[j], self.table[hash_res]
                        hash_res = j
                    j = (j + 1) % TABLE_SIZE
                break
            hash_res = (hash_res + 1) % TABLE_SIZE


hash_set = HashSet()
ans = [str(hash_set.handle_query(line.decode().strip().split())).lower() for line in stdin.buffer.readlines()]
ans = '\n'.join(filter(lambda x: x != '0', ans))
stdout.buffer.write(ans.encode())



