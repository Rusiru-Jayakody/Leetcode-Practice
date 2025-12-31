
class Solution:
    def isSymmetric(self, root) -> bool:
        def dfs(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return dfs(p.left, q.right) and dfs(p.right, q.left)
        return dfs(root.left, root.right)

#This is an alternative soluiton using a deque. We can implement the same using a stack as well

# class Solution:
#     def isSymmetric(self, root) -> bool:
#         d = deque([(root.left,root.right)])
#         while d:
#             p,q = d.popleft()
#             if not p and not q:
#                 continue
#             if not p or not q:
#                 return False
#             if p.val != q.val:
#                 return False
#             d.append((p.left, q.right))
#             d.append((p.right, q.left))
#         return True
    

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
    if not values and values[0] == "null":
        return None
    root = TreeNode(int(values[0]))
    q = deque([root])
    i = 1

    while q and i < len(values):
        node = q.popleft()

        #leftchild
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


#------------------MAIN-------------------------
if __name__ == "__main__":
    sol = Solution()
    print("Enter tree nodes in level order (use 'null' for empty nodes):")
    # Example: 1 2 3 4 5 null null
    values = input().split()
    root = buildTree(values)
    ans = sol.isSymmetric(root)
    print(ans)
        