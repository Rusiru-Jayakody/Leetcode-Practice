
class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        if not root:
            return False
        stk = [(root, 0)]
        while stk:
            node , curr_sum = stk.pop()
            curr_sum += node.val
            if curr_sum == targetSum and not node.left and not node.right:
                return True
            if node.right:stk.append((node.right, curr_sum))
            if node.left:stk.append((node.left,curr_sum))
        return False


#This is an alternative solution using recursive dfs
# class Solution:
#     def hasPathSum(self, root, targetSum: int) -> bool:
#         def dfs(root, curr_sum):
#             if not root:
#                 return False
#             curr_sum += root.val
#             if not root.left and not root.right:
#                 return curr_sum == targetSum
#             return dfs(root.left, curr_sum) or dfs(root.right,curr_sum)
#         return dfs(root,0)



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



#-------------------------MAIN---------------------
if __name__ == "__main__":
    sol = Solution()
    print("Enter tree nodes in level order (use 'null' for empty nodes):")
    # Example: 1 2 3 4 5 null null
    values = input().split()
    target = int(input())
    root = buildTree(values)
    ans = sol.hasPathSum(root,target)
    print(ans)