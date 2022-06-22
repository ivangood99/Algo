from sys import stdin, stdout

MAP_SIZE = 3 * 10 ** 5
MAP_PRIME_NUMBER = MAP_SIZE + 7
SET_SIZE = 100
SET_PRIME_NUMBER = SET_SIZE + 1
MULTIPLIER_NUMBER = 31


class MultiMap:
    def __init__(self):
        self.table = [[] for _ in range(MAP_SIZE)]

    def my_hash(self, obj, type):
        if type == 0:
            prime = MAP_PRIME_NUMBER
            size = MAP_SIZE
        else:
            prime = SET_PRIME_NUMBER
            size = SET_SIZE
        res = 0
        for k in range(len(obj)):
            res = res * MULTIPLIER_NUMBER % prime
            res = (res + ord(obj[k])) % prime
        return res % size

    def handle_query(self, query):
        if query[0][0] == 'p':
            self.put(query[1], query[2])
            return 1
        elif query[0][0] == 'g':
            return self.get(query[1])
        elif query[0] == 'delete':
            self.delete(query[1], query[2])
            return 1
        else:
            self.delete_all(query[1])
            return 1

    def put(self, key, value):
        hash_key = self.my_hash(key, 0)
        hash_value = self.my_hash(value, 1)
        pair_exists_flag = False
        key_ind = -1
        for i in range(len(self.table[hash_key])):
            if self.table[hash_key][i][0] == key:
                key_ind = i
                for j in range(len(self.table[hash_key][i][1][hash_value])):
                    if self.table[hash_key][key_ind][1][hash_value][j] == value:
                        pair_exists_flag = True
                        break
                break
        if key_ind == -1:
            self.table[hash_key].append([key, [[] for _ in range(SET_SIZE)]])
            self.table[hash_key][len(self.table[hash_key]) - 1][1][hash_value].append(value)
        elif not pair_exists_flag:
            self.table[hash_key][key_ind][1][hash_value].append(value)

    def get(self, key):
        hash_key = self.my_hash(key, 0)
        ans = [0, []]
        for i in range(len(self.table[hash_key])):
            if self.table[hash_key][i][0] == key:
                for j in range(len(self.table[hash_key][i][1])):
                    for value in self.table[hash_key][i][1][j]:
                        ans[1].append(value)
                ans[0] = len(ans[1])
                break
        if ans[0] == 0:
            return str(0)
        else:
            return str(ans[0]) + ' ' + ' '.join(ans[1])

    def delete(self, key, value):
        hash_key = self.my_hash(key, 0)
        hash_value = self.my_hash(value, 1)
        for i in range(len(self.table[hash_key])):
            if self.table[hash_key][i][0] == key:
                for j in range(len(self.table[hash_key][i][1][hash_value])):
                    if self.table[hash_key][i][1][hash_value][j] == value:
                        self.table[hash_key][i][1][hash_value].pop(j)
                        break
                break

    def delete_all(self, key):
        hash_key = self.my_hash(key, 0)
        for i in range(len(self.table[hash_key])):
            if self.table[hash_key][i][0] == key:
                self.table[hash_key].pop(i)


multi_map = MultiMap()
ans = [str(multi_map.handle_query(line.decode().strip().split())) for line in stdin.buffer.readlines()]
ans = '\n'.join(filter(lambda x: x != '1', ans))
stdout.buffer.write(ans.encode())