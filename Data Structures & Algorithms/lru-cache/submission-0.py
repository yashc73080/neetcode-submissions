class ListNode:

    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):

        # doubly linked list of max length capacity to track recently used
        # hash map for O(1) lookup

        self.cache = {} # key : ListNode
        self.capacity = capacity

        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        self._remove(node)
        self._add_to_head(node)

        print(f'get {key} -> value: {node.value}')

        return node.value

    def put(self, key: int, value: int) -> None:
        # already in cache, just move it in linked list
        if key in self.cache:
            node = self.cache[key]
            node.value = value

            self._remove(node)
            self._add_to_head(node)
        
        # new key
        else:
            node = ListNode(key, value)
            self.cache[key] = node
            self._add_to_head(node)

            if len(self.cache) > self.capacity:
                lru_node = self.tail.prev
                self._remove(lru_node)

                del self.cache[lru_node.key]


    def _add_to_head(self, node):
        # add next to head
        old_next = self.head.next

        self.head.next = node
        node.prev = self.head

        node.next = old_next
        old_next.prev = node

    def _remove(self, node):
        # cut out node to delete
        old_prev = node.prev
        old_next = node.next

        old_prev.next = old_next
        old_next.prev = old_prev
        