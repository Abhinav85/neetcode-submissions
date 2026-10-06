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
        node_obj = {None: None}
        curr = head
        while curr:
            new_node = Node(curr.val)
            node_obj[curr] = new_node
            curr = curr.next

        curr = head
        while curr:
            new_node = node_obj[curr]
            new_node.next = node_obj[curr.next]
            new_node.random = node_obj[curr.random]
            curr = curr.next
        
        return node_obj[head]

        