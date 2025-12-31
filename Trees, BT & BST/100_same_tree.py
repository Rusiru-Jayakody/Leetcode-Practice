class Solution:
    def isSameTree(self,p,q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right)
    
#This is an alternative soluiton using a deque. We can implement the same using a stack as well
# class Solution:
#     def isSameTree(self, p, q):
#         d = deque([(p,q)])

#         while d:
#             m,n = q.popleft()
#             if not m and not n:
#                 continue
#             if not m or not n:
#                 return False
#             if m.val != n.val:
#                 return False
#             d.append((m.left, n.left))
#             d.append((m.right,n.right))
#         return True



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
    ans = sol.isSameTree(p,q)
    print(ans)
    