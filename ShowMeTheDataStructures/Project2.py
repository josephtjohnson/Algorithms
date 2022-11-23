from asyncio.windows_events import NULL

class DblNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.dict = {}
        self.capactiy = capacity
        self.head = None
        self.tail = None
        self.size = 0


    def remove(self, node):
        if node.key in self.dict:
            if node == self.head:
                self.head = node.next
                node.next.previous = None
                self.size -= 1
            elif node == self.tail:
                self.tail = node.previous
                node.previous.next  = None
                self.size -= 1
            else:
                node.previous.next = node.next
                node.next.previous = node.previous
                self.size -= 1

    def add(self, node):
            if self.head is None:
                self.head = node
                self.tail = self.head
                self.size += 1
            else:
                node.next = self.head
                self.head.previous = node
                self.head = node
                node.previous = None
                self.size += 1

    def keyPresent(self, key):
        return True

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if self.keyPresent(key):
            node = self.dict[key]
            self.remove(node)
            self.add(node)
            return node.value
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key in self.dict:
            node = self.dict[key]
            self.remove(node)
            self.add(node)
        elif self.size == self.capactiy:
            node = self.tail
            self.remove(node)
            self.add(DblNode(key, value))
        else:
            self.add(DblNode(key, value))



our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1

# Test Case 2

# Test Case 3
