# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        ans_head = ans

        carry = 0

        while l1 and l2:
            net_sum = l1.val + l2.val + carry
            ans.next = ListNode(net_sum % 10)
            carry = net_sum // 10
            l1 = l1.next
            l2 = l2.next
            ans = ans.next

        while l1:
            net_sum = l1.val + carry
            ans.next = ListNode(net_sum % 10)
            carry = net_sum // 10
            l1 = l1.next
            ans = ans.next

        while l2:
            net_sum = l2.val + carry
            ans.next = ListNode(net_sum % 10)
            carry = net_sum // 10
            l2 = l2.next
            ans = ans.next

        if carry:
            ans.next = ListNode(carry)

        return ans_head.next




        