# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        it = head
        counter = 0

        while it and counter < k:
            counter += 1 
            it = it.next

        if counter < k:
            return head
        else:
            next_head = self.reverseKGroup(it, k)
            it = head
            stack = [it]
            
            for i in range(k - 1):
                it = it.next
                stack.append(it)

            new_head = it

            while len(stack) > 1:
                it = stack.pop(-1)
                it.next = stack[-1]
            it = stack.pop(-1)
            it.next = next_head

            return new_head

                
                


            
