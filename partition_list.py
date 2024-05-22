# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        node = head
        head_left, head_right =  ListNode(), ListNode()
        it_left, it_right = head_left, head_right
        
        while node:
            if node.val < x:
                it_left.next = node
                it_left = it_left.next
            else:
                it_right.next = node
                it_right = it_right.next
            node = node.next
        
        it_right.next = None
        head_right = head_right.next
        it_left.next = head_right
        head_left = head_left.next
        return head_left

