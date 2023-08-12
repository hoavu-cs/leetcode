# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        it = it_2 = head
        count = 1
        length = 0
        
        while it:
            length += 1
            it = it.next
            if count < n+2:
                count += 1
            else:
                it_2 = it_2.next
                
        if n == length:
            head = head.next
        else:
            it_2.next = it_2.next.next
            
        return head