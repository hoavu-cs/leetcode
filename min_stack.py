from math import inf 

class Node:
    def __init__(self, value, below=None, min_below=None):
        self.value = value
        self.below = below
        self.min_below = min_below


class MinStack:
    def __init__(self):
        self.top_node = Node(value=inf)
        self.min_node = self.top_node
        
    def push(self, val: int) -> None:        
        # add value to the top of the stack
        node = Node(val, below=self.top_node)
        self.top_node = node
        # check if the minimum value changes
        if val < self.min_node.value:
            node.min_below = self.min_node
            self.min_node = node

    def pop(self) -> None:
        node = self.top_node
        if node == self.min_node:
            self.min_node = node.min_below
        self.top_node = node.below

    def top(self) -> int:
        return self.top_node.value
        
    def getMin(self) -> int:
        return self.min_node.value
