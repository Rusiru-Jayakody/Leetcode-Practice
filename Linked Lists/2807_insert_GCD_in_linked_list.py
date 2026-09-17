# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head):
        curr = head
        while curr and curr.next:
            x = curr.val
            y = curr.next.val
            ans = 0
            for i in range(min(x,y)+1,0,-1):
                if x % i == 0 and y % i == 0:
                    ans = i
                    break
            
            temp = ListNode(ans)
            temp.next = curr.next
            curr.next = temp
            curr = temp.next
        
        return head


        