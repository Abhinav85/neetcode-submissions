# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length = length + 1
        
        lff = length - n

        print(lff)

        if (lff == 0):
            return head.next

        prev , curr = None, head

        for i in range(lff):
            prev = curr
            curr = curr.next
        
        #Removal
        prev.next = curr.next
        curr.next = None
        return head
        