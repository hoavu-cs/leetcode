from math import inf
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        it1, it2 = list1, list2
        output = it_merge = ListNode()
        while it1 or it2:
            x1 = x2 = inf
            if it1:
                x1 = it1.val
            if it2:
                x2 = it2.val
            print(f"{x1} {x2}")
            if x1 < x2:
                it_merge.next = it1
                it1 = it1.next 
            else:
                it_merge.next = it2
                it2 = it2.next
            #print(it_merge.val)
            it_merge = it_merge.next
        return output.next
            
            
        