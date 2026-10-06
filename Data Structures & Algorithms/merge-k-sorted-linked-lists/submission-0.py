# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: 

    def mergeTwoLists(self, list1 : [ListNode], list2 : [ListNode])  -> [ListNode]:
        curr1 = list1
        curr2 = list2
        newList = ListNode(0)
        newListHead = newList

        while curr1 and curr2:
            if curr1.val > curr2.val:
                newList.next = ListNode(curr2.val)
                curr2 = curr2.next
            elif curr2.val > curr1.val:
                newList.next = ListNode(curr1.val) 
                curr1 = curr1.next
            else:
                newList.next = ListNode(curr2.val)
                newList = newList.next
                newList.next = ListNode(curr1.val)
                curr2 = curr2.next
                curr1 = curr1.next
            newList = newList.next

        if curr1:
            newList.next = curr1
        
        if curr2:
            newList.next = curr2
        
        return newListHead.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        # Merge lists iteratively, two at a time
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                # Merge two lists or handle single remaining list
                if i + 1 < len(lists):
                    merged_lists.append(self.mergeTwoLists(lists[i], lists[i + 1]))
                else:
                    merged_lists.append(lists[i])
            lists = merged_lists

        return lists[0]


        