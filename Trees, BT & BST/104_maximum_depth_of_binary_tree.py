
class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)
    
    
#Alternative solution using deque(without recurssion), but little slower than the recursive solution
# class Solution:
#     def maxDepth(self,root):
#         if not root:
#             return
#         q = deque([root])
#         depth = 0
#         while q:
#             for _ in range(len(q)):
#                 node = q.popleft()
#                 if node.left : q.append(node.left)
#                 if node.right : q.append(node.right)
#             depth += 1
#         return depth
    

#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.


#Definition for a binary tree node
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
    q = deque([root])
    i = 1

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


# ------------------ MAIN ------------------

if __name__ == "__main__":

    sol = Solution()
    print("Enter tree nodes in level order (use 'null' for empty nodes):")
    # Example: 1 2 3 4 5 null null
    values = input().split()
    root = buildTree(values)
    ans = sol.maxDepth(root)
    print(ans)