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
        hashmap = {}
        
        curr = head
        while curr:
            copy = Node(curr.val)
            hashmap[curr] = copy
            curr = curr.next

        curr = head
        
        while curr:
            new = hashmap.get(curr)
            new.next = hashmap.get(curr.next)
            new.random = hashmap.get(curr.random)
            curr = curr.next
        
        return hashmap.get(head)