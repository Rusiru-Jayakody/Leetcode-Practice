class Solution:
    def isValidBST(self, root) -> bool:
        prev = [None]
        validate = [True]
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if prev[0] is not None and root.val <= prev[0]:
                validate[0] = False
            prev[0] = root.val
            dfs(root.right)
        dfs(root)
        return validate[0]
    
# This is an alternative solution using a stack for the in order depth first search.
# class Solution:
#     def isValidBST(self, root) -> bool:
#         prev = None
#         validate = True
#         curr = root
#         stk = []

#         while stk or curr:
#             while curr:
#                 stk.append(curr)
#                 curr = curr.left
            
#             curr = stk.pop()
#             if prev is not None and curr.val <= prev:
#                 validate = False
#             prev = curr.val
#             curr = curr.right
#         return validate


# This is an alternative solution using min/max bound using iterative dfs..

# class Solution:
#     def isValidBST(self, root) -> bool:
#         if not root:
#             return True
#         stk = [(root, float('-inf'), float('inf'))]
#         while stk:
#             node, minn, maxx = stk.pop()
#             if node.val <= minn or node.val >= maxx:
#                 return False
#             if node.left:stk.append((node.left, minn, node.val))
#             if node.right:stk.append((node.right, node.val, maxx))
#         return True
    
# This is an alternative solution using min/max bound using recursion.

# class Solution:
#     def isValidBST(self, root) -> bool:
#         def dfs(root, minn, maxx):
#             if not root:
#                 return True
#             if root.val <= minn or root.val >= maxx:
#                 return False
            
#             return dfs(root.left, minn, root.val) and dfs(root.right, root.val, maxx)
#         return dfs(root, float('-inf'), float('inf'))



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






#------------------------MAIN----------------------------
if __name__ == "__main__":
    sol = Solution()
    print("Enter tree nodes in level order (use 'null' for empty nodes):")
    # Example: 1 2 3 4 5 null null
    values = input().split()
    root = buildTree(values)
    ans = sol.isValidBST(root)
    print(ans)