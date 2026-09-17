# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head) -> bool:
        d = ListNode()
        d.next = head
        fast = slow = d

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow is fast:
                return True
        return False
        