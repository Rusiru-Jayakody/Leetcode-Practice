# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head, n: int):
        dummy = ListNode()
        dummy.next = head
        ahead = behind = dummy

        for i in range(n+1):
            ahead = ahead.next

        while ahead:
            ahead = ahead.next
            behind = behind.next
        
        behind.next = behind.next.next
        return dummy.next


        