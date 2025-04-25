# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        multiplyer = 1
        #working list 1
        wl1 = l1
        wl2 = l2
        sum = 0
        while wl1 or wl2:
            subsum = 0
            if wl1:
                subsum += wl1.val
                wl1 = wl1.next
            if wl2:
                subsum += wl2.val
                wl2 = wl2.next
            subsum *= multiplyer
            sum += subsum
            multiplyer *= 10
        ans = ListNode()
        current_node = ans
        while True:
            #modulo
            m = sum % 10
            current_node.val = m
            sum -= m
            sum //= 10
            if not sum > 0:
                return ans
            current_node.next = ListNode()
            current_node = current_node.next