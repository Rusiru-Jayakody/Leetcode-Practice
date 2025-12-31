
class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        def sameTree(p,q):
            if not p and not q:
                return True
            if not q or not p:
                return False
            if p.val != q.val:
                return False
            return sameTree(p.left, q.left) and sameTree(p.right,q.right)
        
        def dfs(root):
            if not root:
                return False
            if sameTree(root,subRoot):
                return True
            
            return dfs(root.left) or dfs(root.right)
        
        return dfs(root)
    


# class Solution:
#     def isSubtree(self, root, subRoot) -> bool:
#         if not subRoot:
#             return True
#         if not root:
#             return False
#         d = deque([root])
#         while d:
#             node = d.popleft()
#             if not node:
#                 continue
#             s = deque([(node,subRoot)])
#             matched = True
#             while s:
#                 p,q = s.popleft()
#                 if not p and not q:
#                     continue
#                 if not p or not q:
#                     matched = False
#                     break
#                 if p.val != q.val:
#                     matched = False
#                     break
#                 s.append((p.left,q.left))
#                 s.append((p.right, q.right))
#             if matched:
#                 return True
#             d.append(node.left)
#             d.append(node.right)
#         return False



#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left =None, right = None):
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




#-----------------MAIN-------------------------
if __name__ == "__main__":
    sol = Solution()
    print("Enter tree nodes in level order (use 'null' for empty nodes):")
    # Example: 1 2 3 4 5 null null
    values1 = input().split()
    p = buildTree(values1)
    print("Enter tree nodes in level order (use 'null' for empty nodes):")
    # Example: 1 2 3 4 5 null null
    values2 = input().split()
    q = buildTree(values2)
    ans = sol.isSubtree(p,q)
    print(ans)
        