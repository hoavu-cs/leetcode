from math import inf
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        else:
            left, right  = lists[0 : len(lists)//2], lists[len(lists)//2:] 
            merged_left = self.mergeKLists(left)
            merged_right = self.mergeKLists(right)
            it_left, it_right,  = merged_left, merged_right
            output = it_merged = ListNode()

            while it_left or it_right:
                x = y = inf
                if it_left:
                    x = it_left.val
                if it_right:
                    y = it_right.val
                if x <= y:
                    it_merged.next = it_left
                    it_left = it_left.next
                else:
                    it_merged.next = it_right
                    it_right = it_right.next
                it_merged = it_merged.next

            return output.next
                    


            

