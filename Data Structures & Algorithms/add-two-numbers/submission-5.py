# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        result = dummy
        carry = 0

        while (l1 or l2) or carry > 0:

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sum = carry + val1 + val2
            print (sum)

            if sum <= 9:
                carry = 0
                result.next = ListNode(sum, None)
                result = result.next
            else:
                result.next = ListNode(sum % 10)
                result = result.next
                carry = sum // 10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next