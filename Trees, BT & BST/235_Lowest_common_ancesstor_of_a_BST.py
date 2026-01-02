
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if not root:
                return None
            if p.val > root.val and q.val > root.val:
                return dfs(root.right)
            elif p.val < root.val and q.val < root.val:
                return dfs(root.left)
            else:
                return root
        return dfs(root)
    
#This soluiton is an alternative solution with O(1) extra space
# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         curr = root
#         while curr:
#             if p.val > curr.val and q.val > curr.val:
#                 curr = curr.right
#             elif p.val < curr.val and q.val < curr.val:
#                 curr = curr.left
#             else:
#                 return curr
            


#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right



# --- Helper: Build tree from level-order list ---
from collections import deque
def buildTree(values):
    if not values or values[0] == "null":
        return None
    root = TreeNode(int(values[0]))
    i = 1
    q = deque([root])

    while q and i < len(values):
        node = q.popleft()

        #left child
        if values[i] != "null":
            node.left = TreeNode(int(values[i]))
            q.append(node.left)
        i += 1
        if i >= len(values):
            break

        #right child
        if values[i] != "null":
            node.right = TreeNode(int(values[i]))
            q.append(node.right)
        i += 1
    return root


    # Find references to p and q nodes
def findNode(root, val):
    curr = root
    while curr:
        if curr.val == val:
            return curr
        if val < curr.val:
            curr = curr.left
        elif val > curr.val:
            curr = curr.right
    return None
        



#-----------------------MAIN----------------------
if __name__ == "__main__":
    sol = Solution()
    print("Enter tree nodes in level order (use 'null' for empty nodes):")
    # Example: 1 2 3 4 5 null null
    values = input().split()
    root = buildTree(values)
    p = int(input())
    q = int(input())
    node_p = findNode(root, p)
    node_q = findNode(root, q)
    ans = sol.lowestCommonAncestor(root, node_p, node_q)
    print(ans.val)

        