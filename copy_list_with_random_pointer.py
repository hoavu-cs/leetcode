"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None

        it = head
        random_pointers = {}
        n = 0

        while it:
            n += 1
            it = it.next
        L = [Node(x=0) for i in range(n)] + [None]

        it = head
        i = 0
        
        while it:
            it2 = it.random
            random_position = 0
            while it2:
                random_position += 1
                it2 = it2.next
            random_pointers[i] =  n-random_position
            L[i].val, L[i].next, L[i].random = it.val, L[i+1], L[random_pointers[i]]
            i += 1
            it = it.next

        return L[0]








        



