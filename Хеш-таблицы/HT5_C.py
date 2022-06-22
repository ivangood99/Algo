from sys import stdin, stdout

TABLE_SIZE = 3 * 10 ** 5
PRIME_NUMBER = TABLE_SIZE + 7
MULTIPLIER_NUMBER = 31


class Node:
    def __init__(self, node_data = None, next_node = None, prev_node = None):
        self.data = node_data
        self.next = next_node
        self.prev = prev_node


class LinkedMap:
    def __init__(self):
        self.table = [[] for _ in range(TABLE_SIZE)]
        self.tail = None

    def my_hash(self, obj):
        res = 0
        for k in range(len(obj)):
            res = res * MULTIPLIER_NUMBER % PRIME_NUMBER
            res = (res + ord(obj[k])) % PRIME_NUMBER
        return res % TABLE_SIZE

    def handle_query(self, query):
        if query[0] == 'put':
            self.put(query[1], query[2])
            return 0
        elif query[0] == 'get':
            return self.get(query[1])
        elif query[0] == 'delete':
            self.delete(query[1])
            return 0
        elif query[0] == 'prev':
            return self.prev(query[1])
        else:
            return self.next(query[1])

    def put(self, key, value):
        hash_res = self.my_hash(key)
        exists_flag = False
        prev_size = len(self.table[hash_res])
        for i in range(prev_size):
            if self.table[hash_res][i].data[0] == key:
                self.table[hash_res][i].data[1] = value
                exists_flag = True
                break
        if not exists_flag:
            self.table[hash_res].append(Node(node_data = [key, value], next_node = None, prev_node = self.tail))
            if self.tail is not None:
                self.tail.next = self.table[hash_res][prev_size]
            self.tail = self.table[hash_res][prev_size]

    def get(self, key):
        hash_res = self.my_hash(key)
        size = len(self.table[hash_res])
        for i in range(size):
            if self.table[hash_res][i].data[0] == key:
                return self.table[hash_res][i].data[1]
        return 'none'

    def delete(self, key):
        hash_res = self.my_hash(key)
        size = len(self.table[hash_res])
        for i in range(size):
            if self.table[hash_res][i].data[0] == key:
                if self.table[hash_res][i].prev is not None:
                    self.table[hash_res][i].prev.next = self.table[hash_res][i].next
                if self.table[hash_res][i].next is not None:
                    self.table[hash_res][i].next.prev = self.table[hash_res][i].prev
                else:
                    self.tail = self.table[hash_res][i].prev
                self.table[hash_res].pop(i)
                break


    def prev(self, key):
        hash_res = self.my_hash(key)
        size = len(self.table[hash_res])
        for i in range(size):
            if self.table[hash_res][i].data[0] == key:
                if self.table[hash_res][i].prev is not None:
                    return self.table[hash_res][i].prev.data[1]
        return 'none'

    def next(self, key):
        hash_res = self.my_hash(key)
        size = len(self.table[hash_res])
        for i in range(size):
            if self.table[hash_res][i].data[0] == key:
                if self.table[hash_res][i].next is not None:
                    return self.table[hash_res][i].next.data[1]
        return 'none'


linked_map = LinkedMap()
ans = [str(linked_map.handle_query(line.decode().strip().split())) for line in stdin.buffer.readlines()]
ans = '\n'.join(filter(lambda x: x != '0', ans))
stdout.buffer.write(ans.encode())