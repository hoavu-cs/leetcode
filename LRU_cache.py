class Node():
    def __init__(self, key=None, value=None, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next
    
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.linked_list_head = Node()
        self.linked_list_tail = Node()

        self.linked_list_head.prev = self.linked_list_tail
        self.linked_list_tail.next  = self.linked_list_head

    def move_to_head(self, node):
        previous_node = node.prev
        next_node = node.next
        
        # delete node from the list
        previous_node.next = next_node
        next_node.prev = previous_node

        # put node back at the beginning of the list (most recent)
        first_node = self.linked_list_head.prev
        first_node.next = node
        self.linked_list_head.prev = node
        node.prev = first_node
        node.next = self.linked_list_head

    def insert(self, node):
        first_node = self.linked_list_head.prev
        node.prev = first_node
        node.next = self.linked_list_head
        first_node.next = node
        self.linked_list_head.prev = node

    def remove(self):      
        last_node = self.linked_list_tail.next
        self.linked_list_tail.next = last_node.next
        last_node.next.prev = self.linked_list_tail

        del self.cache[last_node.key]

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.move_to_head(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:      
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.move_to_head(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.insert(node)
            if len(self.cache) > self.capacity: 
                self.remove()

            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
