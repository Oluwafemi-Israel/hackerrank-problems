class Node:
    def __init__(self, key, value, next, prev):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev


class DoubleLinkedList:
    def __init__(self):
        self.head = Node("head", None, None, None)  # Dummy head
        self.tail = Node("tail", None, None, None)  # Dummy tail

        self.head.prev = self.tail
        self.tail.next = self.head

    def add(self, key, value):
        node = Node(key, value, self.head, self.head.prev)

        self.head.prev.next = node
        self.head.prev = node

        return node

    def pop_tail(self):
        """Since there's a dummy tail, this actually pops the node just before the dummy tail"""
        lru = self.tail.next

        self.tail.next = lru.next
        lru.next.prev = self.tail

        return lru

    def move_to_head(self, node):
        """Since there's a dummy head, this actually moves the node to just before the dummy head"""
        node.next.prev = node.prev
        node.prev.next = node.next

        node.next = self.head
        if self.head.prev != node:
            node.prev = self.head.prev
            self.head.prev.next = node
        self.head.prev = node


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.list = DoubleLinkedList()
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.list.move_to_head(node)

            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:

            if len(self.cache) == self.capacity:
                lru = self.list.pop_tail()
                self.cache.pop(lru.key, None)

            node = self.list.add(key, value)
            self.cache[key] = node

        else:
            node = self.cache[key]
            node.value = value

            self.list.move_to_head(node)


if __name__ == "__main__":
    lru_cache = LRUCache(2)
    lru_cache.put(1, 1)
    lru_cache.put(2, 2)
    lru_cache.get(1)
    lru_cache.put(3, 3)
    lru_cache.get(2)
    lru_cache.put(4, 4)
    lru_cache.get(1)
    lru_cache.get(3)
    lru_cache.get(4)
    #
    # lru_cache = LRUCache(1)
    # lru_cache.put(2, 1)
    # lru_cache.get(2)
    # lru_cache.put(3, 2)
    # lru_cache.get(2)
    # lru_cache.get(3)
    #
    # lru_cache = LRUCache(2)
    # lru_cache.put(2, 1)
    # lru_cache.put(2, 2)
    # lru_cache.get(2)
    # lru_cache.put(1, 1)
    # lru_cache.put(4, 1)
    # lru_cache.get(2)
    #
    # lru_cache = LRUCache(2)
    # lru_cache.get(2)
    # lru_cache.put(2, 6)
    # lru_cache.get(1)
    # lru_cache.put(1, 5)
    # lru_cache.put(1, 2)
    # lru_cache.get(1)
    # lru_cache.get(2)

    # lru_cache = LRUCache(2)
    # lru_cache.put(1, 5)
    # lru_cache.put(1, 2)
    # lru_cache.put(2, 6)

    print(lru_cache)
