# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root):

        ans = []

        if not root:
            return ans
            
        stk = []
        stk.append(root)

        while stk:
            n = stk.pop()
            ans.append(n.val)
            if n.right:
                stk.append(n.right)
            if n.left:
                stk.append(n.left)
        
        return ans
        