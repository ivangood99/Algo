from sys import stdin, stdout

TABLE_SIZE = 3 * 10 ** 5
PRIME_NUMBER = TABLE_SIZE + 7
MULTIPLIER_NUMBER = 31


class HashMap:
    def __init__(self):
        self.table = [[] for _ in range(TABLE_SIZE)]

    def my_hash(self, obj):
        res = 0
        for k in range(len(obj)):
            res = res * MULTIPLIER_NUMBER % PRIME_NUMBER
            res = (res + ord(obj[k])) % PRIME_NUMBER
        return res % TABLE_SIZE

    def handle_query(self, query):
        if query[0][0] == 'p':
            self.put(query[1], query[2])
            return 0
        elif query[0][0] == 'g':
            return self.get(query[1])
        else:
            self.delete(query[1])
            return 0

    def put(self, key, value):
        hash_res = self.my_hash(key)
        exists_flag = False
        for i in range(len(self.table[hash_res])):
            if self.table[hash_res][i][0] == key:
                self.table[hash_res][i][1] = value
                exists_flag = True
                break
        if not exists_flag:
            self.table[hash_res].append([key, value])

    def get(self, key):
        hash_res = self.my_hash(key)
        for pair in self.table[hash_res]:
            if pair[0] == key:
                return pair[1]
        return 'none'

    def delete(self, key):
        hash_res = self.my_hash(key)
        for i in range(len(self.table[hash_res])):
            if self.table[hash_res][i][0] == key:
                self.table[hash_res].pop(i)
                break


hash_map = HashMap()
ans = [str(hash_map.handle_query(line.decode().strip().split())) for line in stdin.buffer.readlines()]
ans = '\n'.join(filter(lambda x: x != '0', ans))
stdout.buffer.write(ans.encode())