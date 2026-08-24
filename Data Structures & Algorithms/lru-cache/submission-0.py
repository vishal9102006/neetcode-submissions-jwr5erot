class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        # Dummy nodes
        self.left = Node(0, 0)   # Least Recently Used side
        self.right = Node(0, 0)  # Most Recently Used side

        self.left.next = self.right
        self.right.prev = self.left

    # Remove a node from the linked list
    def remove(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

    # Add node to the right (Most Recently Used)
    def insert(self, node):
        prev = self.right.prev
        next = self.right

        prev.next = node
        node.prev = prev

        node.next = next
        next.prev = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]

            # Mark as recently used
            self.remove(node)
            self.insert(node)

            return node.value

        return -1

    def put(self, key, value):
        if key in self.cache:
            # Remove old node
            self.remove(self.cache[key])

        # Create new node
        node = Node(key, value)
        self.cache[key] = node

        # Add as most recently used
        self.insert(node)

        # If capacity exceeded
        if len(self.cache) > self.capacity:
            # Remove least recently used node
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]