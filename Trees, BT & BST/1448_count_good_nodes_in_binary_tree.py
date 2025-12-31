
class Solution:
    def goodNodes(self, root) -> int:
        good = 0
        stk = [(root, float('-inf'))]
        while stk:
            node, largest = stk.pop()
            if node.val >= largest:
                good += 1
                largest = node.val
            if node.right:stk.append((node.right,largest))
            if node.left:stk.append((node.left,largest))
        return good
    


#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0,left = None, right = None):
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
    i =1

    while q and i < len(values):
        node = q.popleft()

        #left child
        if values[0] != "null":
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

#This is an alternative solution using recursive dfs
# class Solution:
#     def goodNodes(self, root: TreeNode) -> int:
#         def dfs(root,max_so_far):
#             if not root:
#                 return 0
#             good = 1 if root.val >= max_so_far else 0

#             max_so_far = max(max_so_far, root.val)

#             return good + dfs(root.left,max_so_far) + dfs(root.right, max_so_far)
#         return dfs(root, float('-inf'))



#---------------MAIN---------------------------
if __name__ == "__main__":
    sol = Solution()
    print("Enter tree nodes in level order (use 'null' for empty nodes):")
    # Example: 1 2 3 4 5 null null
    values = input().split()
    root = buildTree(values)
    ans = sol.goodNodes(root)
    print(ans)
        
        