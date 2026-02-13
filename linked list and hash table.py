class Node:
    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def put(self, k, v):
        idx = hash(k) % self.size
        self.table[idx] = Node(k, v, self.table[idx])

    def get(self, k):
        curr = self.table[hash(k) % self.size]
        while curr:
            if curr.key == k:
                return curr.val
            curr = curr.next
        return None


ht = HashTable(5)
ht.put("ID_1", "Alice")
print(ht.get("ID_1"))

